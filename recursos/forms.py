from dal import autocomplete
from django import forms

from recursos.models import *


class DetalleDelRecursoForm(forms.ModelForm):
    class Meta:
        model = DetalleDelRecurso
        fields = ('__all__')
        widgets = {
            "caracteristica": autocomplete.ModelSelect2(url='/admin/recursos/caracteristicaautocomplete/'),
        }

class TipoDeRecursoForm(forms.ModelForm):
    class Meta:
        model = TipoDeRecurso
        fields = ('__all__')
        widgets = {
            "encargado": autocomplete.ModelSelect2(url='/admin/recursos/encargadoderecursoautocomplete/'),
        }