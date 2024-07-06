import os
import django
from django.core.exceptions import ValidationError

from main_app.models import Book

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions
