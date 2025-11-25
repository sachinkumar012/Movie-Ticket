from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from .models import Movie, Show, Booking
from .serializers import (
    MovieSerializer, ShowSerializer, BookingSerializer,
    SignupSerializer, LoginSerializer, BookSeatSerializer
)

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': {'username': user.username, 'email': user.email},
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ShowListView(generics.ListAPIView):
    serializer_class = ShowSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Show.objects.filter(movie_id=movie_id)

class BookSeatView(generics.CreateAPIView):
    serializer_class = BookSeatSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        show = get_object_or_404(Show, pk=self.kwargs['show_id'])
        context['show'] = show
        return context

    def perform_create(self, serializer):
        show = self.get_serializer_context()['show']
        seat_number = serializer.validated_data['seat_number']
        Booking.objects.create(
            user=self.request.user,
            show=show,
            seat_number=seat_number
        )

class CancelBookingView(generics.UpdateAPIView):
    queryset = Booking.objects.filter(status='booked')
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        booking = self.get_object()
        if booking.user != request.user:
            return Response({'error': 'Not your booking'}, status=status.HTTP_403_FORBIDDEN)
        booking.status = 'cancelled'
        booking.save()
        serializer = self.get_serializer(booking)
        return Response(serializer.data)

class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
