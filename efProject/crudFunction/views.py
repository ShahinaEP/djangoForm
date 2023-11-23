from django.shortcuts import redirect, render
from app.models import *
from .forms import *
# Create your views here.
def banner_list(request):
    banner = BannerSection.objects.all()
    return render(request, 'crudFunction/banner_list.html',{'banner':banner})

def banner_view(request, pk):
    banner = BannerSection.objects.get(pk = pk)
    return render(request, 'crudFunction/banner-view.html',{'banner':banner})

def banner_add(request):
    if request.method == 'POST':
        form = BannerFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form2 =BannerFrom()
        context ={
            'form' : form2
        }
        return render(request, 'crudFunction/banner_add.html', context)
        
def banner_edit(request, pk):
    banner = BannerSection.objects.get(pk = pk)
    print(banner)
    if request.method == 'POST':
        form = BannerFrom(request.POST, request.FILES, instance= banner)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form2 =BannerFrom(instance=banner)
        context ={
            'form' : form2
        }
        return render(request, 'crudFunction/banner_add.html', context)
    

def banner_delete(request, pk):
    banner = BannerSection.objects.get(pk = pk)
    banner.delete()
    return redirect('banner_list')
        
