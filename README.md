# Movie Ticket Booking System

A Django-based web application for booking movie tickets online.

## Setup

1. **Clone and navigate:**
   ```bash
   git clone <repository-url>
   cd movie-ticket
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Populate database (optional):**
   ```bash
   python seed_script.py
   ```

6. **Run server:**
   ```bash
   python manage.py runserver
   ```

## Approach

- **Models:** Movie, Show, Booking with relationships
- **API:** REST endpoints using Django REST Framework
- **Authentication:** Django's built-in user system
- **Database:** SQLite for development
- **Seed Script:** Populates database with sample data

## Features

- Movie listings
- Show scheduling
- Seat booking
- User management
