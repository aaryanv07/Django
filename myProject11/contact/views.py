
from django.shortcuts import render,redirect 
# pyrefly: ignore [missing-import]
from django.http import HttpResponse
from .models import Contact

def contact_form(request):
    return render(request,'contact.html')
def submit_contact(request):
    if request.method == "GET":
        name=request.GET.get('name')
        # email=request.GET.get('email')
        message=request.GET.get('message')
        # Contact.objects.create(name=name,email=email,message=message)
        if name and message:
            Contact.objects.create(name=name,message=message)
            return HttpResponse(f"Thank you {name}, for your message")
        else:
         return HttpResponse("Please provide all the fields")
    return redirect('contact_form')