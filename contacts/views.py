from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        contact = Contact(name=name, email=email, phone=phone,  date=date)
        contact.save()
        
       
    
    return redirect(index)