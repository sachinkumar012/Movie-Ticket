from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Movie, Show, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    available_seats = serializers.SerializerMethodField()

    class Meta:
        model = Show
        fields = '__all__'

    def get_available_seats(self, obj):
        return obj.available_seats()

class BookingSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='show.movie.title', read_only=True)
    screen_name = serializers.CharField(source='show.screen_name', read_only=True)
    date_time = serializers.DateTimeField(source='show.date_time', read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class BookSeatSerializer(serializers.Serializer):
    seat_number = serializers.IntegerField()

    def validate_seat_number(self, value):
        show = self.context['show']
        if value < 1 or value > show.total_seats:
            raise serializers.ValidationError("Invalid seat number")
        if Booking.objects.filter(show=show, seat_number=value, status='booked').exists():
            raise serializers.ValidationError("Seat already booked")
        return value
