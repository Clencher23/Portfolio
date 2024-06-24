from django.contrib import admin
from django.urls import path, include
from home import views



# Django admin header customization
admin.site.site_header = "DevBatman"
admin.site.site_title = "Greetings"
admin.site.index_title = "random stuff"

urlpatterns = [
    path('',  views.home, name='home'),
    path('about',  views.about, name='about'),
    path('projects',  views.projects, name='projects'),
    path('contact',  views.contact, name='contact'),
]