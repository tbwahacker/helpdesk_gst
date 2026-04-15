from django.contrib import admin
from .models import User, Category, Ticket, Comment, Attachment, Report, KnowledgeBase


# -------------------------
# User Admin
# -------------------------
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)


# -------------------------
# Category Admin
# -------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


# -------------------------
# Ticket Admin
# -------------------------
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'user', 'assigned_to', 'created_at')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')


# -------------------------
# Comment Admin
# -------------------------
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'created_at')


# -------------------------
# Attachment Admin
# -------------------------
@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'uploaded_at')


# -------------------------
# Report Admin
# -------------------------
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'generated_by', 'generated_at')


# -------------------------
# Knowledge Base Admin
# -------------------------
@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')