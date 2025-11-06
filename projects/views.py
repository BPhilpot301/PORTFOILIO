from django.shortcuts import render
from . import models


# Create your views here.

#def about_me_view(request):
#    return render(request, 'portfolio/about_me.html')

#def experience_view(request):
#    return render(request, 'portfolio/experience.html')


def projects_view(request):
    projects_list = models.Project.objects.all()
    context = {'projects': projects_list}
    return render(request, 'projects/projects.html',context)

#def contact_view(request):
#    return render(request, 'portfolio/contact.html')