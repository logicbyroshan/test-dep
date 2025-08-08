from django.shortcuts import render
from .models import MyInfo, Project, Skill

def home(request):
    home = MyInfo.objects.last()
    projects = Project.objects.all()[0:3]
    skills = Skill.objects.all()[:3]
    return render(request, 'portfolio/home.html', {'home':home, 'projects':projects, 'skills':skills})

def project(request):
    return render(request, 'portfolio/projects.html')

def blog(request):
    return render(request, 'portfolio/blogs.html')

def exp(request):
    return render(request, 'portfolio/blogs.html')