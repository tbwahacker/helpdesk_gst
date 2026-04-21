from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),

]