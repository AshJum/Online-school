# Online School

**Online School** is a simple Django-based web application for online education. It supports multiple user roles (students, teachers, and superusers) and includes core functionality for virtual classrooms, lesson scheduling, and student performance tracking.

## Features

- **User Authentication** with role-based access (student, teacher, admin)
- **Video Lessons**: Superusers can upload video content via the admin panel; students can view lessons
- **Grading System**: Teachers can assign grades to students; students can view their own grades
- **Schedule Management**: Teachers can create class schedules; students can view their upcoming lessons
- **Teacher Profiles**: Teachers can list additional skills and information

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AshJum/Online-school.git
   cd Online-school

   Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Start the development server:

python manage.py runserver

Open your browser and go to:

    http://127.0.0.1:8000/

Usage

    Admins (superusers) can log in to /admin/ to upload lessons and manage users.

    Teachers have access to grading and scheduling tools.

    Students can view their grades and schedules.
