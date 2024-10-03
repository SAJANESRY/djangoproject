from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('',views.index),
    path('about/',views.aboutview),
    path('registration/',views.registrationview,name='registration'),
    path('login/',LoginView.as_view(template_name='login.html'),name='Login'),
]