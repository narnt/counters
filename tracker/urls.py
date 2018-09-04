from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_counters, name='all_counters'),
    path('counter/<int:pk>/', views.counter_edit, name='counter_edit'),
    path('new/', views.new_counter, name='new_counter'),
    path('counter/<int:pk>/remove/', views.counter_remove, name='counter_remove'),
    path('auth/registration', views.register, name='register'),
]