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
class TipoDeRecursoListView(ListView):
	"""
	View lista de tipos de recurso, sobreescribiendo la vista propia del admin
	"""
	model = TipoDeRecurso
	template_name = "tipoderecurso_list.html"

	def get_queryset(self):
		tipos_de_recurso = TipoDeRecurso.objects.all()

		q = self.request.GET.get('q', '')
		if q != '':
			tipos_de_recurso = tipos_de_recurso.filter( nombre__icontains=q )

		return tipos_de_recurso

	def render_to_response(self, context, **response_kwargs):
		if 'excel' in self.request.GET.get('excel', ''): 
			lista_datos=[]
			datos = self.get_queryset()
			for dato in datos:
				lista_datos.append([dato.nombre])

			titulos=[ 'Nombre' ]
			return listview_to_excel(lista_datos,'Tipos de recursos',titulos)
		
		return super(TipoDeRecursoListView, self).render_to_response(context, **response_kwargs)

	def get_context_data(self, **kwargs):
		context = super(TipoDeRecursoListView, self).get_context_data(**kwargs)
		context['q'] = self.request.GET.get('q', '')
		return context

	@method_decorator(staff_member_required)
	def dispatch(self, *args, **kwargs):
		return super(TipoDeRecursoListView, self).dispatch(*args, **kwargs)

class RecursoListView(ListView):
	"""
	View lista de recursos, sobreescribiendo la vista propia del admin
	"""
	model = Recurso
	template_name = "recurso_list.html"

	def get_queryset(self):
		recursos = Recurso.objects.all()

		q = self.request.GET.get('q', '')
		if q != '':
			recursos = recursos.filter( Q(codigo__startswith=q) | Q(nombre__icontains=q) | Q(observaciones__icontains=q) )

		tipoderecurso_id = self.request.GET.get('tipoderecurso_id', '')
		if tipoderecurso_id != '':
			recursos = recursos.filter(tipo_id=tipoderecurso_id)

		encargado_id = self.request.GET.get('encargado_id', '')
		if encargado_id != '':
			recursos = recursos.filter(tipo__encargado_id=encargado_id)

		estado = self.request.GET.get('estado', 'TODOS')
		if estado == 'DISPONIBLE':
			recursos = recursos.filter(estado=0)
		elif estado == 'MANTENIMIENTO':
			recursos = recursos.filter(estado=1)
		elif estado == 'RESERVADO':
			recursos = recursos.filter(estado=2)
		elif estado == 'EN_USO':
			recursos = recursos.filter(estado=3)

		return recursos

	def render_to_response(self, context, **response_kwargs):
		if 'excel' in self.request.GET.get('excel', ''): 
			lista_datos=[]
			datos = self.get_queryset()
			for dato in datos:
				lista_datos.append([dato.codigo, dato.nombre, dato.tipo.nombre, dato.tipo.encargado.get_full_name(), dato.get_estado_display()])

			titulos=[ 'Codigo','Nombre', 'Tipo','Encargado','Estado' ]
			return listview_to_excel(lista_datos,'Recursos',titulos)
		
		return super(RecursoListView, self).render_to_response(context, **response_kwargs)

	def get_context_data(self, **kwargs):
		context = super(RecursoListView, self).get_context_data(**kwargs)
		context['q'] = self.request.GET.get('q', '')
		context['tiposderecurso'] = TipoDeRecurso.objects.all()
		context['tipoderecurso_id'] = int(self.request.GET.get('tipoderecurso_id','')) if (self.request.GET.get('tipoderecurso_id','') != '') else ''

		context['encargados'] = User.objects.filter(groups__name='Encargado de recursos')
		context['encargado_id'] = int(self.request.GET.get('encargado_id', '')) if (self.request.GET.get('encargado_id', '') != '') else ''

		context['estado'] = self.request.GET.get('estado', 'TODOS')

		return context
		
	@method_decorator(staff_member_required)
	def dispatch(self, *args, **kwargs):
		return super(RecursoListView, self).dispatch(*args, **kwargs)

class RecursoDetailView(DetailView):
	model = Recurso
	template_name = "recurso_detail.html"

	@method_decorator(staff_member_required)
	def dispatch(self, *args, **kwargs):
		return super(RecursoDetailView, self).dispatch(*args, **kwargs)

@login_required
def recursos_presentacion(request):
	context = RequestContext(request)
	titulo="RECURSOS"
	descripcion="."
	return render_to_response('admin/presentacion.html', {'titulo':titulo,'descripcion':descripcion}, context)



