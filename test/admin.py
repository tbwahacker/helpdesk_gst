from django.contrib import admin

from test.models import Test, Ticket, Category, Notification, Comment, Assignment

# Register your models here.
admin.site.register(Test)
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Assignment)
admin.site.register(Notification)
admin.site.register(Category)