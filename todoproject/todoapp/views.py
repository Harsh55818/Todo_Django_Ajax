from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        usr = User(name=request.POST['name'], marks=request.POST['marks']).save()
        return redirect('/')
    else:
        print('Something wrong!')

def show(request):
    usr = User.objects.all()
    return render(request, 'result.html', {'usr': usr})

def delete(request, pk):
    if request.method == 'POST':
        usr = User.objects.get(pk=pk)
        usr.delete()
        return redirect('/')

def edit(request, pk):
    usr = User.objects.get(pk=pk)
    content = {
        'usr': usr
    }
    return render(request, 'edit.html', content)

def update(request, pk):
    usr = User.objects.get(pk=pk)
    usr.name = request.POST['name']
    usr.marks = request.POST['marks']
    usr.save()
    return redirect('/')


