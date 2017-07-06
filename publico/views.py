from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q

from django.contrib.auth.models import User, Group

from recursos.models import *
from extra.globals import listview_to_excel

from django.http import Http404
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
#from common.jasper import reportes

# Create your views here.
class RecursoPublicoListView(ListView):
	"""
	View lista de recursos, sobreescribiendo la vista propia del admin
	"""
	model = Recurso
	template_name = "recurso_publico_list.html"

	def get_queryset(self):
		recursos = Recurso.objects.all()

		q = self.request.GET.get('q', '')
		if q != '':
			recursos = recursos.filter( Q(codigo__startswith=q) | Q(nombre__icontains=q) | Q(observaciones__icontains=q) )

		tipoderecurso_id = self.request.GET.get('tipoderecurso_id', '')
		if tipoderecurso_id != '':
			recursos = recursos.filter(tipo_id=tipoderecurso_id)

		return recursos

	def render_to_response(self, context, **response_kwargs):
		if 'excel' in self.request.GET.get('excel', ''):
			lista_datos=[]
			datos = self.get_queryset()
			for dato in datos:
				lista_datos.append([dato.codigo, dato.nombre, dato.observaciones])

			titulos=[ 'Codigo','Nombre', 'observaciones' ]
			return listview_to_excel(lista_datos,'Recursos',titulos)

		return super(RecursoPublicoListView, self).render_to_response(context, **response_kwargs)

	def get_context_data(self, **kwargs):
		context = super(RecursoPublicoListView, self).get_context_data(**kwargs)
		context['q'] = self.request.GET.get('q', '')
		context['tiposderecurso'] = TipoDeRecurso.objects.all()
		context['tipoderecurso_id'] = int(self.request.GET.get('tipoderecurso_id','')) if (self.request.GET.get('tipoderecurso_id','') != '') else ''
		return context
