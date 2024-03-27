from django.urls import path
from . import views


urlpatterns = [
    path("", views.about, name="about"),
    path("about/", views.about, name="about"),
    path("resume/", views.experience, name="experience"),
    path("projects/", views.professional, name="professional"),
    path("contact/", views.contact, name="contact")
]
