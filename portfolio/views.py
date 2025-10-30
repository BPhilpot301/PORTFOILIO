from django.shortcuts import render

def about_me_view(request):
    return render(request, 'portfolio/about_me.html')

def experience_view(request):
    return render(request, 'portfolio/experience.html')

def contact_view(request):
    return render(request,'portfolio/contact.html')