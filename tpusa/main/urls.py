from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("events/", views.events, name="events"),
    path("contact/", views.contact, name="contact"),
    path("join/", views.join, name="join"),
    path("leadership/", views.leadership, name="leadership"),
]
