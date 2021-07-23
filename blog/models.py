from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.urls import reverse


class matlabs(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    mohtava = models.TextField()
    updatedatetime = models.DateTimeField(('create date'), auto_now_add=True, auto_now=False)
    createdatetime = models.DateTimeField(('update date'), auto_now_add=False, auto_now=True)

    def human_readable_title(self):
        return self.title.replace(' ', '_')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id':self.id})