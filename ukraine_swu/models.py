from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
      
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    header = models.CharField(max_length=100, default='none')
    text = models.TextField()
    budget = models.IntegerField(default=0)
    full_text = models.TextField()
    rich_text = RichTextField(default="Text")
    image = models.TextField(default='https://media.sproutsocial.com/uploads/2017/02/10x-featured-social-media-image-size.png')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    photo = models.TextField()