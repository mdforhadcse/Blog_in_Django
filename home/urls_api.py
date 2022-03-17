from django.urls import path
# from .views import *
from . import views_api

urlpatterns = [
    path('login/', views_api.LoginView, ),
    path('register/', views_api.RegisterView, ),

]
