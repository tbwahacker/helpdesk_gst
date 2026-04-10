from django.db import models


class Test(models.Model):
    column1=models.TextField()
    column2=models.IntegerField(default=0)
    column3=models.CharField(unique=True, null=False)
    column4=models.DateField(auto_now=True)

class Ticket(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=30)
    status = models.TextField(max_length=10)
    priority = models.CharField()
    created_by = models.CharField()
    assigned_to = models.TextField()
    category_id = models.TextField(unique=True, null=False)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    ticket_id = models.CharField(unique=True, null=False)
    user_id = models.CharField(unique=True, null=False)
    message = models.TextField(max_length=100)
    created_at = models.DateField(auto_now=True)

class Notification(models.Model):
        user_id = models.CharField(unique=True, null=False)
        message = models.TextField(max_length=100)
        is_read = models.CharField()
        created_at = models.DateField(auto_now=True)

class Assignment(models.Model):
     ticket_id = models.CharField(unique=True, null=False)
     agent_id = models.CharField(unique=True, null=False)
     assigned_by = models.TextField(max_length=30)
     assigned_at = models.DateField(auto_now=True)

class Category(models.Model):
      name = models.TextField(max_length=20)
