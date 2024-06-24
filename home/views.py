from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    context = {'Name': 'Aman', 'Course': 'Django'}
    return render(request, 'home.html', context)
    # return HttpResponse("this is my homepage (/)")

def about(request):

    return render(request, 'about.html')
    # return HttpResponse("this is my about page (/about)")

def projects(request):
    return render(request, 'projects.html')
    # return HttpResponse("this is my projects page (/projects)")

def contact(request):
    if request.method == "POST":
           
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone'] 
        desc = request.POST['desc']   
        print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data has been written into DB")
    return render(request, 'contact.html')
    # return HttpResponse("this is my contact (/contact)")