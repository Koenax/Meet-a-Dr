# Meet-a-Dr 💼👩‍⚕️👨‍⚕️
### ALX Final Project 🎓

## Overview 📝

Meet-a-Dr is a web platform that connects clients seeking medical services with doctors providing those services. The project features a variety of functionalities for guests, registered patients and doctors,  ensuring a smooth user experience for all.

## Features ✨

#### Website (Guests) 👥
Guests can:
- **Browse the Homepage**: Get an overview of the platform and navigate to other sections 🏡
- **Register/Login**: Create an account or log in to access personalized features 🔑
- **Explore Categories**: View different medical service categories for better navigation 🏷️

#### Logged-In Users Seeking Services (Clients) 💁‍♀️💁‍♂️
Clients can:
- **Search for Doctors**: Find doctors based on specialties, availability, and location 🔍
- **View Doctor Profiles**: Access detailed profiles of doctors with services offered, reviews, and availability 📜
- **Personal Dashboard**: Track appointments, view history, and manage medical records 🩺

#### Logged-In Users Offering Services (Doctors) 👩‍⚕️👨‍⚕️
Doctors can:
- **Manage Appointments**: Schedule, modify, and track patient consultations 📅
- **Patient Interaction**: View patient details, treatment plans, and medical records 📝
- **Update Services**: Offer new services, adjust availability, and update personal profiles 💼

#### Admin Panel 🛠️
Admins can:
- **Manage Users**: Approve or disapprove client and doctor profiles ✔️❌
- **Monitor Platform Activity**: Track user interactions, appointments, and platform health 📊
- **Generate Reports**: Generate reports on usage, services, and platform statistics 📈


## Installation 🛠️

### Django Backend Installation (with Docker)

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Koenax/Meet-a-Dr.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Meet-a-Dr
    cd BACKEND
    ```

3. **Create a `.env` file** (if necessary):
    Ensure you have the required environment variables.

4. **Build and start the Docker containers**:
    Make sure you have Docker and Docker Compose installed, then run:
    ```bash
    docker-compose up --build
    ```

    This will:
    - Build the Docker images for the Django backend and PostgreSQL database.
    - Start the containers for the Django app and PostgreSQL database.

5. **Run database migrations**:
    After the containers are up, run the migrations to set up your database:
    ```bash
    docker-compose exec backend python manage.py migrate
    ```

6. **Access the Django backend**:
    Once the containers are running, you can access the Django backend at [http://localhost:8000](http://localhost:8000) 🌍

#### React Frontend Installation

1. **Clone the repository**:
    If you haven’t already, clone the repository as shown above

2. **Navigate to the React frontend directory**:
    ```bash
    cd FRONTEND
    ```

3. **Install dependencies**
    ```bash
    npm install
    ```

    This will install all the required dependencies for the React app.

4. **Start the React development server**:
    Run the following command to start the React app locally:
    ```bash
    npm run dev
    ```

    This will start the React development server at [http://localhost:3000](http://localhost:3000).

5. **Access the React frontend**:
    Open your browser and navigate to [http://localhost:3000](http://localhost:3000) to view the frontend🌍

## Tech Stack 🖥️🔧

- **Backend**: Django (Python) 🐍 - A robust framework for building web applications.
- **Frontend**: React, HTML, CSS 🎨 - A modern and responsive frontend to ensure a smooth user interface.
- **Database**: PostgreSQL 🗄️ - A powerful, open-source relational database for handling application data.
- **Authentication**: JWT / Session-based Authentication (depending on your implementation) 🔐 - Secure user authentication for different roles (patients, doctors, admins).

## URLs 🌐

- **Homepage**: [http://localhost:8000](http://localhost:8000) 🏠 - Entry point for all users.
- **Admin Panel**: [http://localhost:8000/admin](http://localhost:8000/admin) — Fully functional for admin users ✅
- **Doctors API**: [http://localhost:8000/api/doctors/](http://localhost:8000/api/doctors/) — Endpoint for accessing doctor data 💻
- **API Authentication**: [http://localhost:8000/api/auth/](http://localhost:8000/api/auth/) — Endpoint for user authentication 🔌

## Future Improvements 🚀

- **Search Functionality**: Implement advanced search options to filter doctors based on specialties, availability, and ratings 🔍
- **Messaging System**: Add real-time messaging for communication between clients and doctors 💬
- **Appointment Scheduling**: Enable clients to schedule, reschedule, and cancel appointments directly 📅
- **Doctor Ratings & Reviews**: Introduce a rating system for clients to leave feedback on doctors 🌟

## License 📜

This project is licensed under the MIT License — see the LICENSE file for more details. ⚖️
