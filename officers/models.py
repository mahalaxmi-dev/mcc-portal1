from django.db import models


DEPARTMENT_CHOICES = [
    ('Sanitation', 'Sanitation'),
    ('Roads & Infrastructure', 'Roads & Infrastructure'),
    ('Water Supply', 'Water Supply'),
    ('Drainage', 'Drainage'),
    ('Street Lights', 'Street Lights'),
    ('Parks & Public Spaces', 'Parks & Public Spaces'),
]


class Officer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    department = models.CharField(
        max_length=100,
        choices=DEPARTMENT_CHOICES
    )

    def __str__(self):
        return f"{self.name} - {self.department}"


class LoginLog(models.Model):
    officer_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.login_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.officer_name} - {formatted_time}"