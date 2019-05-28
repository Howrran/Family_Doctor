from django.urls import  path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    path('',views.index),
    path('users/', views.get_users),
    path('register/', views.register),
    path('register/login', views.LoginFormView.as_view()),
    path('profile/', views.profile),
    path('timetable/', views.timetable),
    path('our_doctors/', views.our_doctors),
    path('department/', views.department),
    ]

urlpatterns += staticfiles_urlpatterns()