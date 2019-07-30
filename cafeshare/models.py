from django.db import models
from django.contrib.auth.models import User

class Cafe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to="image/")
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.title  

class Comment(models.Model):
    cafe = models.ForeignKey('Cafe',on_delete=models.CASCADE,related_name='comments')
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=100)
    comment_contents = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
