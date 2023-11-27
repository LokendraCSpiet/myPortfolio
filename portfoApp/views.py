from django.shortcuts import render, redirect
from django.http import HttpResponse
from portfoApp.models import pf_contact
# from .models import *
from django.contrib import messages



# Create your views here.
def Home_portfolio(request):
    return render(request,'home.html')

def about_me(request):
    return render(request,'about.html')

def my_resume(request):
    return render(request,'resume.html')

def my_contact(request):
    return render(request,'contact.html')

def my_portfolio(request):
    return render(request,'portfolio.html')

def online_portfolio(request):
    return render(request,'onlinePort.html')

def online_about(request):
    return render(request,'onAbout.html')

def online_Services(request):
    return render(request,'onServices.html')

def online_Portfolio(request):
    return render(request,'onPortfolio.html')

def header(request):
    return render(request,'common_Header.html')

def projects(request):
    return render(request,'projects.html')

def submit_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        pdsave = pf_contact(
            full_name=name,
            email=email,
            subject=subject,
            message=message
        )
        pdsave.save()
        messages.success(request, 'Submitted successfully!')
        return redirect('contact')
        # return HttpResponse("Form submitted successfully!")
    messages.success(request, 'Something Went Wrong!!!')
    return render(request,'home.html')
    # return HttpResponse("GET request, please submit the form.")

