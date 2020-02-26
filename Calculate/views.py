from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):

    if request.method == 'POST' :
        input_1 = int(request.POST['input_1'])
        input_2 = int(request.POST['input_2'])
        result = input_1 + input_2
    return render(request, 'home.html',{'result':result})
