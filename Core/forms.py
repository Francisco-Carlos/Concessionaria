from django import forms
from .models import Veiculos, Images, Marcas

class MarcasForm(forms.ModelForm):
    class Meta:
        model = Marcas
        fields = ('Marca',)
        widgets = {
            'Marca':forms.TextInput(attrs={'class':'form-control'})
        }

class VeiculosForm(forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = ['Nome','Marca','Preco','Ano', 'Imagem']
        widgets ={
            'Nome': forms.TextInput(attrs={'class':'form-control'}),
            'Marca': forms.Select(attrs={'class':'form-control'}),
            'Preco': forms.NumberInput(attrs={'class':'form-control'}),
            'Ano':  forms.DateInput(attrs={'class':'form-control'}),
            'Imagem': forms.FileInput(attrs={'class':'form-control','multiple':True})
        }

class ImagemForm(forms.ModelForm):
    Imagens = forms.ImageField(label="imagem", widget=forms.ClearableFileInput(attrs={'multiple':True}))

    class Meta():
        model = Images
        fields = ['imagens',]