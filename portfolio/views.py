from django.shortcuts import render
from . import models
from .forms import ContactForm
from django.core.mail import send_mail

def about_me_view(request):
    return render(request, 'portfolio/about_me.html')

def experience_view(request):
    return render(request, 'portfolio/experience.html')

def contact_view(request):
    return render(request,'portfolio/contact.html')

def projects_view(request):
    return render(request, 'projects/projects.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            message_body =(
                f'You have a new email from your portfolio'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message: {message}\n'
                )

            try:
                send_mail(
                    "Email from portfolio",
                    message_body,
                    email,
                    ['britphilpot43@gmail.com']
                )
                print("did this work?")    
                form = ContactForm()
                return render(request, 'portfolio/contact.html', {'form':form})
            except Exception as e:
                print(f'Error sending email: {e}')
                return render(request, 'portfolio/contact.html', {'form':form})

        else:
                print("Invalid data")
    else:
        form = ContactForm()
        return render(request, 'portfolio/contact.html', {'form':form})


      