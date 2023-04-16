from django.contrib import admin
from django.urls import path,include

from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('addition',views.addition,name="addition"),
    path('registration',views.registration,name="registration"),
    path('welcome',views.welcome,name="welcome"),
    path('delete_stud',views.delete_stud,name="delete_stud"),
    path('edit_stud',views.edit_stud,name="edit_stud"),
    path('update_data',views.update_data,name="update_data"),
    path('login',views.login,name="login"),
    path('login_check',views.login_check,name="login_check"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.logout,name="logout"),
    path('addcookie',views.addcookie,name="addcookie"),
    path('getcookie',views.getcookie,name="getcookie")
]
