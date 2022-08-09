from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from . import helper

# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=20)
  
    
    class Meta:
        ordering=("name",)

    def __str__(self):
        return self.name

class Room(models.Model):       
    name=models.CharField(max_length=1000)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True,blank=True,related_name="topic")
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="host")
    title=models.TextField(max_length=10000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    participants=models.ManyToManyField(User,related_name="participants",blank=True)
    slug=models.SlugField(default="",null=True)

    class Meta:
        ordering=("-created",)
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(helper.randoms() + " " + self.name)
        super().save(*args,**kwargs)

class Message(models.Model):
    message_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="message_by")
    body=models.TextField(max_length=10000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name="room")
    slug=models.SlugField(default="",null=True)
    
    class Meta:
        ordering=("-created",)

    def save(self,*args,**kwargs):
        self.slug=slugify(helper.randoms() + " " + self.message_by.username)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.body

class Reply(models.Model):
    reply_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="reply_by")
    body=models.TextField(max_length=10000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    message=models.ForeignKey(Message,on_delete=models.CASCADE,related_name="replies",null=True)
    slug=models.SlugField(default="",null=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(helper.randoms() + " " + self.reply_by.username )
        super().save(*args,**kwargs)

    class Meta:
        verbose_name_plural="Replies" 
        ordering=("-created",)  

class Profile(models.Model):
    profile=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    image=models.ImageField(upload_to="xmedia",null=True)
    cover_image=models.ImageField(upload_to="xmedia",null=True,blank=True)
    followers=models.ManyToManyField(User,related_name="followers",blank=True)
    following=models.ManyToManyField(User,related_name="following",blank=True)
    slug=models.SlugField(default=" ",null=True)
    residence=models.CharField(max_length=1000,default="Not set")
    created=models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.profile.username} profile"

    def save(self,*args,**kwargs):
        self.slug=slugify("user" + " " + self.profile.username)
        super().save(*args,**kwargs)

class Notification(models.Model):
    user_profile=models.ForeignKey(Profile,related_name="notifications",on_delete=models.CASCADE,null=True)
    user_space=models.ForeignKey(User,on_delete=models.CASCADE,related_name="notification",null=True)
    content=models.CharField(max_length=1000)
    link=models.CharField(max_length=1000)
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender",null=True)
    time_sent=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=("-time_sent",)

class Latest(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name="latest")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="personal")
    display=models.CharField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    link=models.CharField(max_length=1000)

    class Meta:

        ordering=("-created",)
class PrivateMessage(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="private")
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_dm")
    content=models.CharField(max_length=2000)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=("-created",)

