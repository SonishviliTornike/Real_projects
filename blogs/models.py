from django.db import models
from django.contrib.auth.models import User

# If you need to extend the User model, you can create a Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username
