from django.shortcuts import render, redirect, get_object_or_404
from .models import Crismando
from .forms import CrismandoForm

# Create your views here.
def main_crismando(request):
    crismandos = Crismando.objects.all()
    return render(request, 'crismando/main_crismando.html', {'crismandos': crismandos})


def novo_crismando(request):
    if request.method == 'POST':
        form = CrismandoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('main_crismando')
        else:
            print(form.errors)
    else:
        form = CrismandoForm()
    return render(request, 'crismando/novo_crismando.html',{'form': form})


def filtrar_crismando(request):
    crismandos = Crismando.objects.all()
    print(request.POST.get('input_nome'))
    ##if nome:
    ##    crismandos = crismandos.objects.filter(nome=nome)
    return render(request, 'crismando/main_crismando.html', {'crismandos': crismandos})