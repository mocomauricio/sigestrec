from dal import autocomplete
from django import forms

from recursos.models import *


class DetalleDelRecursoForm(forms.ModelForm):
    """
    Formulario de detalle de recursos con widgets personalizados
    """
    class Meta:
        model = DetalleDelRecurso
        fields = ('__all__')
        widgets = {
            "caracteristica": autocomplete.ModelSelect2(url='/admin/recursos/caracteristicaautocomplete/'),
        }

class TipoDeRecursoForm(forms.ModelForm):
    """
    Formulario de tipo de recursos con widgets personalizados
    """
    class Meta:
        model = TipoDeRecurso
        fields = ('__all__')
        widgets = {
            "encargado": autocomplete.ModelSelect2(url='/admin/recursos/encargadoderecursoautocomplete/'),
        }