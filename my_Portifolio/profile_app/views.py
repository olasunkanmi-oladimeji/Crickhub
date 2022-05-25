from email import message
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings

# Create your views here.

def home(request):
    #form_class = ContactForm
    if request.method == 'Get':
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        
        if form.is_valid():
            '''subject = request.POST.get('subject')
            name = request.POST.get('name')
            email_address = request.POST.get ('email_address')
            message = request.POST.get('message')'''
            print("vail form")
            
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email_address = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, f'{name},{email_address},{message}', settings.EMAIL_HOST_USER, ['oladimeji.olasunkanmi321@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('success')
            '''try:
            
                send_mail(subject, text_message, settings.EMAIL_HOST_USER, ['oladimeji.olasunkanmi321@gmail.com']) 
            
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')'''
			
    return render(request,'index.html', {'form':form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')