from django.shortcuts import render
from .models import History

# Create your views here.
def home(request):
    return render(request, 'home.html')

def calculate(request):
    if request.method == 'POST' :
        input_1 = float(request.POST['input_1'])
        input_2 = float(request.POST['input_2'])
        History.object.create(x = input_1, y = input_2)
        if 'add' in request.POST:
            result = input_1 + input_2
            op = '+'
            History.object.create(operator = op)
        elif 'sub' in request.POST:
            result = input_1 - input_2
            op = '-'
            History.object.create(operator = op)
        elif 'multiple' in request.POST:
            result = input_1 * input_2
            op = '*'
            History.object.create(operator = op)
        elif 'divide' in request.POST:
            result = input_1 / input_2
            op = '/'
            History.object.create(operator = op)

        History.object.create(result = result)
        history_calculate = History.objects.all()
    return render(request, 'home.html',{'result':result,'history_calculate':history_calculate})
