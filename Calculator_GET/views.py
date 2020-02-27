from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homeGET.html')

def calculate(request):
    if request.method == 'GET' :
        input_1 = int(request.GET['input_1'])
        input_2 = int(request.GET['input_2'])
        if 'add' in request.GET:
            result = input_1 + input_2
        elif 'sub' in request.GET:
            result = input_1 - input_2
        elif 'multiple' in request.GET:
            result = input_1 * input_2
        elif 'divide' in request.GET:
            result = input_1 / input_2
    return render(request, 'homeGET.html',{'result':result})
