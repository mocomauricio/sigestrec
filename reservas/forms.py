from dal import autocomplete
from django import forms

from reservas.models import *
from datetime import datetime    


class ReservaForm(forms.ModelForm):
    """
    Formulario de Reservas utilizado por el encargado de recursos
    """
    class Meta:
        model = Reserva
        fields = ('__all__')
        widgets = {
            "recurso": autocomplete.ModelSelect2(url='/admin/reservas/reservarecursoautocomplete/', forward=['tipo_recurso']),
            "solicitante":  autocomplete.ModelSelect2(url='/admin/sistema/usuarioautocomplete/'),
        }

    def clean(self):
        cleaned_data = super(ReservaForm, self).clean()
        hora_inicio = cleaned_data.get("hora_inicio")
        hora_fin = cleaned_data.get("hora_fin")
        if hora_inicio > hora_fin:
            msg = "hora de inicio no puede ser mayor que hora de finalizacion"
            self.add_error('hora_inicio', msg)







class MiReservaForm(forms.ModelForm):
    """
    Formulario de Mis Reservas utilizado por los usuarios no administrativos
    """
    class Meta:
        model = MiReserva
        exclude =  ['solicitante',]
        widgets = {
            "recurso": autocomplete.ModelSelect2(url='/admin/reservas/reservarecursoautocomplete/', forward=['tipo_recurso']),
        }

    def clean(self):
        cleaned_data = super(MiReservaForm, self).clean()
        hora_inicio = cleaned_data.get("hora_inicio")
        hora_fin = cleaned_data.get("hora_fin")
        if hora_inicio > hora_fin:
            msg = "hora de inicio no puede ser mayor que hora de finalizacion"
            self.add_error('hora_inicio', msg)


class EntregarRecursoGeneralForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('tipo_recurso','recurso',)
        widgets = {
            "recurso": autocomplete.ModelSelect2(url='/admin/reservas/reservarecursogeneralautocomplete/', forward=['tipo_recurso']),
        }

    def __init__(self, *args, **kwargs):
        super(EntregarRecursoGeneralForm, self).__init__(*args, **kwargs)
        self.fields['tipo_recurso'].widget = forms.HiddenInput()
        self.fields['tipo_recurso'].widget.attrs['readonly'] = True
        self.fields['recurso'].widget.attrs['required'] = True

        

    def save(self, commit=True):
        reserva = super(EntregarRecursoGeneralForm, self).save(commit=False)
        reserva.entregado = True
        reserva.fecha_hora_entrega = datetime.now()

        recurso = reserva.recurso
        recurso.estado = 3 #en uso

        if commit:
            reserva.save()
            recurso.save()

        return reserva