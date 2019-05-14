from django.urls import  path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    path('',views.Helo),
    path('users/', views.get_users),
    path('register/', views.RegisterFormView.as_view()),
    path('register/login', views.LoginFormView.as_view()),

    ]

urlpatterns += staticfiles_urlpatterns()