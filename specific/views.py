from django.shortcuts import render

# Create your views here.
def nag(request):
    return render(request,'nag.html')

def gani(request):
    return render(request,'gani.html')