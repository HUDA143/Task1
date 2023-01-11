from django.urls import path
from . import views

app_name = 'bankapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('newbutton/', views.newbutton, name='newbutton'),
    path('form/', views.form, name='form'),

]
