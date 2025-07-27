from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.templatetags.static import static
from django.conf import settings
import os


# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return f"{self.title} - {self.company}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    def get_profile_picture_url(self):
        if self.profile_picture:
            file_path = os.path.join(settings.MEDIA_ROOT, str(self.profile_picture))
            if os.path.exists(file_path) and self.profile_picture.name != 'default.jpg':
                return self.profile_picture.url
        return static('website/default.jpg')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    



#model for collaborative filteing
class UserJobInteraction(models.Model):
    INTERACTION_CHOICES = [
        ('viewed', 'Viewed'),
        ('saved', 'Saved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_link = models.URLField()
    company_name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.interaction_type} - {self.job_title}"
