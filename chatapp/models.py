from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    content  = models.TextField()
    file = models.FileField(upload_to='File')
    status = models.BooleanField('Approved', default=False)
    date_asked = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.question)

class answers(models.Model):
    author=models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    answers = models.TextField()
    file = models.FileField(upload_to= 'Answers')
    staus = models.BooleanField(default= 'False')
    ate_answered = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.question)