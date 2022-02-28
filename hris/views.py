from django.shortcuts import render

def dashboard(request):
    return render(request, 'hris/dashboard.html')

def projects(request):
    return render(request, 'hris/projects.html')