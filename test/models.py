from django.db import models


class Test(models.Model):
    column1=models.TextField(max_length=10)
    column2=models.IntegerField(default=0)
    column3=models.CharField(max_length=10)
    column4=models.DateField(auto_now=True)

class Ticket(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=30)
    status = models.TextField(max_length=10)
    priority = models.IntegerField(default=0)
    created_by = models.CharField(max_length=10)
    assigned_to = models.TextField(max_length=10)
    category_id = models.TextField(unique=True, null=False)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    ticket_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    message = models.TextField(max_length=100)
    created_at = models.DateField(auto_now=True)

class Notification(models.Model):
    user_id = models.CharField(max_length=10)
    message = models.TextField(max_length=100)
    is_read = models.CharField(max_length=5)
    created_at = models.DateField(auto_now=True)

class Assignment(models.Model):
    ticket_id = models.CharField(max_length=10)
    agent_id = models.CharField(max_length=10)
    assigned_by = models.TextField(max_length=30)
    assigned_at = models.DateField(auto_now=True)

class Category(models.Model):
    name = models.TextField(max_length=20)
