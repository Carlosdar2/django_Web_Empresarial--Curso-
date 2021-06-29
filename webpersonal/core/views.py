from django.shortcuts import render,HttpResponse
def base(request):
    return render(request,'core/base.html')

# Create your views here.
def home(request):
    return render(request, "core/home.html")
 

def about(request):
    return render(request,'core/about.html')
def portafolio(request):
    return render(request,'core/portafolio.html')
def Contact(request):
    return render(request,'core/contact.html')