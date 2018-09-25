from django.shortcuts import render, redirect, get_object_or_404
from .models import Crismando
from .forms import CrismandoForm

# Create your views here.
def main_crismando(request):
    return render(request, 'crismando/main_crismando.html')

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
