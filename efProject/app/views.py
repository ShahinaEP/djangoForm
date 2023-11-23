from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    bannerData = BannerSection.objects.all() 
    Product = ProductList.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        submit = Contact(name=name, email= email, phone=phone, message=message)
        submit.save()
        return redirect('home')
    context ={
        "data":bannerData,
        'products':Product
    }
    return render(request, 'home.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render (request, 'contact.html', context)

def contact2(request):
    form = ContactForm2()
    if request.method == 'POST':
        form =ContactForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render (request, 'contact2.html', context)