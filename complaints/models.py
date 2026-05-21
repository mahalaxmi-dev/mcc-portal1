from django.db import models
from users.models import Citizen

class Complaint(models.Model):

    DEPARTMENT_CHOICES = [
        ('Sanitation', 'Sanitation'),
        ('Roads & Infrastructure', 'Roads & Infrastructure'),
        ('Water Supply', 'Water Supply'),
        ('Drainage', 'Drainage'),
        ('Street Lights', 'Street Lights'),
        ('Parks & Public Spaces', 'Parks & Public Spaces'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    complaint_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    description = models.TextField()
    map_location = models.CharField(max_length=100, blank=True, null=True)
    attachment = models.ImageField(upload_to='complaints/attachments/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date_submitted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    officer_remark = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.complaint_id} - {self.title}"