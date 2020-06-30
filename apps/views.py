from django.shortcuts import render
from .models import settings

def index(request):
    template = 'index.html'
    context = {}
    context['obj'] = settings.objects.all()[0]
    context['range'] = range(1,context['obj'].number_of_inputs+1)
    return render(request,template,context)

def script_out(request):
    template = 'output.html'
    context = {}
    obj = settings.objects.all()[0]
    a = []
    for i in range(1,obj.number_of_inputs+1):
        a.append(int(request.POST['number_'+str(i)]))
    b = []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if obj.maximum_number < (a[i]+a[j]):
                pass
            else:
                b.append(a[i]+a[j])
            if obj.maximum_number < abs(a[i]-a[j]):
                pass
            else:
                b.append(abs(a[i]-a[j]))
    print(b)
    b.sort()
    a = {'up':[],'down':[]}
    for i in b:
        if i <= (obj.maximum_number/2):
            if i not in a['down']:
                a['down'].append(i)
                a['down'].append('-')
        else:
            if i not in a['up']:
                a['up'].append(i)
                a['up'].append('-')
    a['down'] = a['down'][0:len(a['down'])-1]
    a['up'] = a['up'][0:len(a['up'])-1]
    context['obj'] = a
    print(a)
    return render(request,template,context)