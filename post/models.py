from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    is_published = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title