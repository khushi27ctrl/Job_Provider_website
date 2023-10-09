from django.contrib import admin
from django.urls import path
from my_app import views
urlpatterns = [
   path("",views.index,name='my_app'),
   path("about",views.about,name='about'),
   path("jobs",views.jobs,name='jobs'),
   path("contact",views.contact,name='contact'),
   path('registration',views.registration,name="registration"),
   path('signin',views.signin,name='signin'),
   path("login",views.login,name='login'),
   path('home',views.home,name='home'),
]
