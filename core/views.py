from django.shortcuts import render
from .models import About, Education, Experience, Professional

# Create your views here.


def about(request):
    about_page = About.objects.all()
    return render(request, 'core/about.html', {"about_page": about_page})


def experience(request):
    experience_page = Experience.objects.all()
    education_page = Education.objects.all()
    return render(request, "core/resume.html", {"experience_page": experience_page, "education_page": education_page})


def professional(request):
    professional_page = Professional.objects.all()
    return render(request, "core/projects.html", {"projects": professional_page})

