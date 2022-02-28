from django.shortcuts import render
from django.contrib import messages
from .models import UserT, WorkerT, ProjectT, AssignmentT, EvaluationReportT

def demo(request):
    return render(request, 'hris/demo.html')

def projects(request):
    project_objects = ProjectT.objects.all()
    return render(request, 'hris/projects.html', {'projects':project_objects})

def add_project(request):
    #code here
    return render(request, 'hris/add_project.html')