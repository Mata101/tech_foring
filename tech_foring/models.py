from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Decided to use default User table 
# class Users(models.Model):
#     username = models.CharField(max_length=20,unique=True)
#     email = models.CharField(max_length=64,unique=True)
#     password = models.CharField(max_length=64)
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     date_joined = models.DateTimeField()


class Projects(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectMembers(models.Model):
    Role = [
        ("Admin", "Admin"),
        ("Member", "Member")
    ]
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role =  models.CharField(max_length=10,choices=Role)

class Tasks(models.Model):
    STATUS_CHOICES = [
        ("To Do","To Do"),
        ("In Progress","In Progress"),
        ("Done","Done")
    ]
    Priority = [
        ("Low","Low"),
        ("Medium","Medium"),
        ("High","High")
    ]
    title = models.CharField(max_length=64)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20,choices=Priority)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    project= models.ForeignKey(Projects,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField()

class Comments(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.ForeignKey(Tasks,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    