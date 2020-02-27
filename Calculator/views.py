from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def calculator(request):
    return render(request, 'calculate/home.html')

def calaulatorGET(request):
    return render(request, 'homeGET.html')