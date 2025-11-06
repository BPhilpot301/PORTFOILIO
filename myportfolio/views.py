from django.shortcuts import render


def home_view(request):
    return render(request, 'base.html')

def about_me_view(request):
    return render(request, 'about_me.html')

def experience_view(request):
    return render(request, 'experience.html')

def projects_view(request):
    return render(request, 'projects.html')