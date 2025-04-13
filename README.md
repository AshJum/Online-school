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

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run migrations:
   ```bash
   python manage.py migrate

4. Create a superuser:
   ```bash
   python manage.py createsuperuser

5. Start the development server:
   ```bash
   python manage.py runserver

6. Open your browser and go to:
   ```bash
    http://127.0.0.1:8000/

 ## Usage

   Admins (superusers) can log in to /admin/ to upload lessons and manage users.

   Teachers have access to grading and scheduling tools.

   Students can view their grades and schedules.
