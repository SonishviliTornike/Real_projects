from django.db import models
from django.contrib.auth.models import User

# If you need to extend the User model, you can create a Profile 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username
    


class BlogStories(models.Model):
    img = models.ImageField(upload_to=None, max_length=2000)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

