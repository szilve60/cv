from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.index, name='index'),
    path('en/', views.english_index, name='english_index'),
]
