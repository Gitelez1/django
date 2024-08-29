# login_app/models.py
from django.db import models
import re
import bcrypt
from datetime import datetime, timedelta

class UserManager(models.Manager):
    def validate_registration(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        # First Name validation
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if not post_data['first_name'].isalpha():
            errors['first_name'] = "First name should contain letters only"
        
        # Last Name validation
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if not post_data['last_name'].isalpha():
            errors['last_name'] = "Last name should contain letters only"
        
        # Email validation
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email format"
        if User.objects.filter(email=post_data['email']).exists():
            errors['email_unique'] = "Email already registered"
        
        # Password validation
        if len(post_data['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if post_data['password'] != post_data['confirm_password']:
            errors['password_match'] = "Passwords do not match"
        
        # Birthday validation (SENSEI BONUS)
        if 'birthday' in post_data:
            try:
                birthday = datetime.strptime(post_data['birthday'], '%Y-%m-%d')
                if birthday > datetime.now():
                    errors['birthday'] = "Birthday must be in the past"
                elif (datetime.now() - birthday).days < 13 * 365:
                    errors['birthday'] = "You must be at least 13 years old to register"
            except ValueError:
                errors['birthday'] = "Invalid birthday format"

        return errors

    def validate_login(self, post_data):
        errors = {}
        user = User.objects.filter(email=post_data['email'])
        if not user:
            errors['email'] = "Invalid email"
        elif not bcrypt.checkpw(post_data['password'].encode(), user[0].password.encode()):
            errors['password'] = "Invalid password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

