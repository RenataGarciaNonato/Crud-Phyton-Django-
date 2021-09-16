from django.shortcuts import render, redirect
from app.forms import PacienteForm
from app.models import Paciente


# Create your views here.
def home(request):
    data={}
    data['db']= Paciente.objects.all() #para pegar todos os dados
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data ['form'] = PacienteForm
    return render(request, 'form.html', data)


def create(request):
    form=PacienteForm(request.POST or None) # vai pegar os dados dos post
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data ={}
    data['db']=Paciente.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db']=Paciente.objects.get(pk=pk)
    data['form']=PacienteForm(instance=data['db'])
    return render(request, 'form.html', data)

def update (request, pk):
    data = {}
    data['db'] =Paciente.objects.get(pk=pk)
    form= PacienteForm(request.POST or None, instance=data ['db'])
    if form.is_valid():
        form.save
    return redirect('home')

def delete (request, pk):
    db = Paciente.objects.get(pk=pk)
    db.delete()
    return redirect('home')






