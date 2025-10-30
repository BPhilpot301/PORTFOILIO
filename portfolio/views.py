from django_shortcuts import render

def about_me_view(request):
    return render(request, 'portfolio/about_me.html')

def experience_view(request):
    return render(request, 'portfolio/experience.html')
