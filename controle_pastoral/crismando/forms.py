from django import forms
from .models import Crismando


class CrismandoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    nome_pai = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nome_mae = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    batismo = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    eucaristia = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    ano_crisma = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Crismando
        fields = ['nome', 'data_nascimento', 'nome_pai', 'nome_mae', 'batismo', 'eucaristia', 'ano_crisma']