from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def calculate(request):
    if request.method == 'POST' :
        input_1 = int(request.POST['input_1'])
        input_2 = int(request.POST['input_2'])
        if 'add' in request.POST:
            result = input_1 + input_2
        elif 'sub' in request.POST:
            result = input_1 - input_2
        elif 'multiple' in request.POST:
            result = input_1 * input_2
        elif 'divide' in request.POST:
            result = input_1 / input_2
    return render(request, 'home.html',{'result':result})
