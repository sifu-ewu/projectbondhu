from pyexpat import features
from unicodedata import name
from django.db import models
from django import forms
import uuid
from users.models import Profile
# Create your models here.
class Tag(models.Model):
 name = models.CharField(max_length=200)
 created_at = models.DateTimeField(auto_now_add=True)
 id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
 def __str__(self):
        return self.name
class doctor(models.Model):
    name = models.CharField(max_length=200,null=False, blank=False)
    specialty = models.CharField(max_length=200,null=False, blank=False)
    certification_CHOICES = (
        ('A', 'American Board'),
        ('B', 'Bachelor'),
    )
    tags = models.ManyToManyField(Tag,blank=True)
    certification = models.CharField(max_length=30, choices=certification_CHOICES)
    description = models.TextField(null=True, blank=True)
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)
    
    def __str__(self):
     return str(self.name)
    
class Project(models.Model):
    user = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor,null=True,blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True,default="default.jpg")
    demo_link = models.CharField(max_length=2000,null=True, blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    tags = models.ManyToManyField(Tag,blank=True)
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title
class reviews(models.Model):
    VOTE_CHOICES = (
        ('up','Up Vote'),
        ('down','Down Vote'),
    )
    #owner =
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.TextField(max_length=200,choices=VOTE_CHOICES)
    
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.value





