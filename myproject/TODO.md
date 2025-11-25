# Movie Ticket Booking System - TODO

## 1. Models
- [x] Create Movie model (title, duration_minutes)
- [x] Create Show model (movie FK, screen_name, date_time, total_seats)
- [x] Create Booking model (user FK, show FK, seat_number, status, created_at)

## 2. Serializers
- [x] Create serializers.py
- [x] MovieSerializer
- [x] ShowSerializer
- [x] BookingSerializer
- [x] SignupSerializer
- [x] LoginSerializer
- [x] BookSeatSerializer

## 3. Views
- [x] SignupView (POST /signup)
- [x] LoginView (POST /login)
- [x] MovieListView (GET /movies/)
- [x] ShowListView (GET /movies/<id>/shows/)
- [x] BookSeatView (POST /shows/<id>/book/)
- [x] CancelBookingView (POST /bookings/<id>/cancel/)
- [x] MyBookingsView (GET /my-bookings/)

## 4. URLs
- [x] Configure myapp/urls.py with API patterns
- [x] Configure myproject/urls.py with swagger and app include

## 5. Settings
- [x] Add REST_FRAMEWORK config for JWT authentication
- [x] Add SPECTACULAR_SETTINGS for swagger

## 6. Migrations
- [x] Run makemigrations
- [x] Run migrate

## 7. README
- [x] Create README.md with setup instructions, API usage, swagger link

## 8. Testing
- [ ] Test server startup
- [ ] Test signup/login
- [ ] Test movie/show endpoints
- [ ] Test booking logic (prevent double booking, overbooking)
- [ ] Test cancellation
- [ ] Verify swagger docs
