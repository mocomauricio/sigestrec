from dal import autocomplete
from django import forms

from mantenimientos.models import *

class MantenimientoForm(forms.ModelForm):
    """
    Formulario de tipo de recursos con widgets personalizados
    """
    class Meta:
        model = Mantenimiento
        fields = ('__all__')
        widgets = {
            "recurso": autocomplete.ModelSelect2(url='/admin/recursos/recursoautocomplete/'),
        }