from django.contrib import admin
from django.urls import path,include

from .import views

urlpatterns = [
    # Navigation Bar
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path('log_in', views.log_in, name="log_in"),
    path('log_out', views.log_out, name="log_out"),
    path('edit_profile', views.edit_profile, name="edit_profile"),

    path('insert/<int:id>', views.insert, name='insert'),
    path('list/<int:id>', views.list, name='list'),
    path('update/<int:id>', views.update, name='update'),
    path('update_data/<int:id>', views.update_data, name='update_data'),
    path('show_data', views.show_data, name="show_data"),
    path('delete/<int:id>', views.delete, name='delete'),

    path('home',views.home, name="home"),
    path('about',views.about, name="about"),
    path('matches',views.matches, name="matches"),

    path('view_profile', views.view_profile, name="view_profile"),
    path('viewed_profile', views.viewed_profile, name="viewed_profile"),
    path('profile',views.profile, name="profile"),
    path('viewed_not_contacted',views.viewed_not_contacted, name="viewed_not_contacted"),
    path('members',views.members, name="members"),
    path('shortlisted',views.shortlisted, name="shortlisted"),



]