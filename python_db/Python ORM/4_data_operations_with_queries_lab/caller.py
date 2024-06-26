import os
import django
from datetime import date, datetime

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Run and print your queries
from main_app.models import Student


def add_students():
    student_data = [
        ('FC5204', 'John', 'Doe', '15/05/1995', 'john.doe@university.com'),
        ('FE0054', 'Jane', 'Smith', 'NULL', 'jane.smith@university.com'),
        ('FH2014', 'Alice', 'Johnson', '10/02/1998', 'alice.johnson@university.com'),
        ('FH2015', 'Bob', 'Wilson', '25/11/1996', 'bob.wilson@university.com')
    ]

    for student in student_data:
        student_id, first_name, last_name, birth_date, email = student

        if birth_date != 'NULL':
            birth_date = datetime.strptime(birth_date, '%d/%m/%Y').date()
        else:
            birth_date = None

        student_obj = Student(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            email=email
        )

        student_obj.save()


def get_students_info():
    students_info = Student.objects.all()
    lines = [
        f'Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}'
        for student in students_info
    ]
    return '\n'.join(lines)


def update_students_emails():
    students_info = Student.objects.all()
    for student in students_info:
        student.email = student.email[:-14] + 'uni-students.com'
        student.save()


def truncate_students():
    students = Student.objects.all()
    students.delete()


truncate_students()
print(Student.objects.all())
print(f'Number of students: {Student.objects.count()}')