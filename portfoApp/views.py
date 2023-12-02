from django.shortcuts import render, redirect
from django.http import HttpResponse
from portfoApp.models import pf_contact
# from .models import *
from django.contrib import messages

from django.http import JsonResponse
import json



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

""" 
def datatable_view(request):
    people = pf_contact.objects.all()
    data = []

    for person in people:
        data.append({
            'full_name': person.full_name,
            'email': person.email,
            'subject': person.subject,
            'message': person.message,
        })

    return JsonResponse(data, safe=False)
 """

def datatable_view(request):
    try:
        people = pf_contact.objects.all()
        data = []

        for person in people:

            if(person.status == 1):
                status = "Checked"
            elif(person.status == 2):
                status = "Un-checked"
            elif(person.status == 0):
                status = "pending"

            data.append({
                'Id': person.id,
                'full_name': person.full_name,
                'email': person.email,
                'subject': person.subject,
                'message': person.message,
                'status': status,
            })

        return JsonResponse({'data': data}, safe=False)
    except Exception as e:
        print(f"Error in datatable_view: {e}")
        return JsonResponse({'error': 'Internal Server Error'}, status=500)


def checked_contact(request):
    id = request.POST.get('id')
    pfContact_instance = pf_contact.objects.get(id=id)
    # mydata = pf_contact.objects.filter(id=id).values()
    # print(mydata[0]['full_name'])
    # print(my_model_instance.full_name)
    pfContact_instance.status = 1
    pfContact_instance.save()
    result = {
        'data':pfContact_instance.id,
        'msg':"Contact Checked Successfully"
        }
    return JsonResponse(result)
    # return JsonResponse({'id': model.id, 'name': model.name})

def delete_contact(request):
    id = request.POST.get('id')
    pfContact_instance = pf_contact.objects.get(id=id)
    pfContact_instance.delete()
    result = {
        'msg':"Contact Deleted Successfully"
        }
    return JsonResponse(result)