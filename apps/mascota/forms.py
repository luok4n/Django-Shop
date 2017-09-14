from django import forms

from apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		fields = [
			'nombre',
			'precio',
			'cantidad',
			'color',
			'marca',
		]
		labels = {
			'nombre': 'Nombre',
			'precio': 'Precio',
			'cantidad': 'Cantidad',
			'color':'Color',
			'marca': 'Marca',
		}
		widgets = {
			'Nombre': forms.TextInput(attrs={'class':'form-control'}),
			'Precio': forms.TextInput(attrs={'class':'form-control'}),
			'Cantidad': forms.TextInput(attrs={'class':'form-control'}),
			'Color': forms.TextInput(attrs={'class':'form-control'}),
			'Marca': forms.CheckboxSelectMultiple(),
		}