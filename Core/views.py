from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .forms import MarcasForm,ImagemForm,VeiculosForm
from .models import Marcas,Images,Veiculos
# Create your views here.


def Index(request):
    return render(request,'Index.html')

def Buscar(request):
    veiculos = Veiculos.objects.all()

    if 'Buscar' in request.GET:
        Nome_Da_Busca = request.GET['Buscar']
        if Buscar:
            Lista_Buscar = veiculos.filter(Nome__icontains=Nome_Da_Busca)

    dados = {'veiculos':Lista_Buscar}
    return render(request,'Index.html',dados)

#ver os detalhes do veiculo
def Detalhes(request,car_id):
    veiculos = Veiculos.objects.get(id=car_id)
    dados = {'veiculos':veiculos}
    return render(request,'Detalhes.html',dados)


def Cadastrar(request):
    if request.POST:
        veiculo = VeiculosForm(request.POST,request.FILES)
        files = request.FILES.getlist('Imagem')
        img = list
        if veiculo.is_valid():
            veiculo.save()
            return redirect('Cadastrar')
    else:
        veiculo = VeiculosForm
        context = {'veiculo':VeiculosForm}

    return render(request,'Cadastrar.html',{'veiculo':veiculo})

def CadstMarca(request):
    if request.POST:
        marca = MarcasForm(request.POST)
        if marca.is_valid():
            marca.save()
            return redirect('Cadastrar')
    else:
        marca = MarcasForm

    return render(request,'Marcas.html',{'marca':marca})

def Consecionaria(request):
    veiculos = Veiculos.objects.order_by('-Ano').all()
    dados = {'veiculos':veiculos}
    return render(request,'Veiculos.html',dados)
