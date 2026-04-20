from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('verify-users/', views.verify_users, name='verify_users'),
    path('approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject-user/<int:user_id>/', views.reject_user, name='reject_user'),
]