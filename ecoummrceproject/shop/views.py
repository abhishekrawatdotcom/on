from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product,contact

def index(request):
    products=product.objects.all()

    return render(request,'index.html',{'product':products})


def about(request):
    return render(request,'about.html')

def contactview(request):
    if request.method=='POST':
        print(request)
        name=request.POST.get('name','')

        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        print(name,email,phone,desc)
        count=contact(name=name,email=email,phone=phone,desc=desc)
        count.save()

    return render(request,'contact.html')

def traker(request):
    return render(request,'traker.html')

def productview(request, myid):
    prod=product.objects.filter(id= myid)
    print(prod)

    return render(request,'productview.html',{'prodd':prod})

def search(request):
    return render(request,'search.html')

def checkout(request):
    return render(request,'checkout.html')


# Create your views here.
