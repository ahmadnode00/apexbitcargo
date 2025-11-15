from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('tracker/', views.tracker_form, name='tracker'),  # tracking form
    path('tracker/result/', views.tracking_result, name='tracking_result'),  # tracking result
]
