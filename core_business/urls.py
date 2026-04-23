from django.urls import path

from core_business import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket', views.ticket, name='ticket'),
    path('account/', views.account_view, name='account')
]