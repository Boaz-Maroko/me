from django.shortcuts import render, redirect
from time import sleep

from .forms import ContactForm
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


def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # print(contact_form)
            contact_form.save()
            sleep(2)
            return redirect('contact')
        else:
            contact_form = ContactForm()

    return render(request, "core/contact.html", {"contact_form": contact_form})

