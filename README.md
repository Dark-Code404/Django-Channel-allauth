# Simple Chat App Using Django Channels

## Overview

This project demonstrates the implementation of a simple chat application using various technologies, including Django Channels, WebSockets, Django Allauth for authentication and email verification, Redis for in-memory caching, and SQLite with Django's built-in ORM.

## Technologies Used

- **Django Channels**: For handling WebSockets and real-time communication.
- **WebSockets**: For enabling real-time communication between the client and server.
- **Django Allauth**: For user authentication and email verification.
- **Redis**: For in-memory caching to improve performance.
- **SQLite**: As the database, managed using Django's built-in ORM.

## Features

- Real-time chat functionality using WebSockets.
- User authentication and email verification with Django Allauth.
- In-memory caching with Redis to enhance performance.
- SQLite database managed through Django's ORM for simplicity.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/simple-chat-app.git
   cd simple-chat-app`
   ```
2. **Install Dependencies:**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Migrations:**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Start the Development Server:**:
   ```bash
   python manage.py runserver
   ```




***For more detail guide on django channels , web socket and all auth read their respective official documentation.***




**Samples:**



![channel1](https://github.com/user-attachments/assets/8ceb199d-d845-409f-ba73-31e78996fc7d)
![channel2](https://github.com/user-attachments/assets/be40a830-3375-4659-a7e7-771445957717)

