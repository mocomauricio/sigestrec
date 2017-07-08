from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q

from django.contrib.auth.models import User, Group

from recursos.models import *
from reservas.models import *
from mantenimientos.models import *
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




class ReservaPublicoListView(ListView):
	"""
	View lista de reservas, sobreescribiendo la vista propia del admin
	"""
	model = Reserva
	template_name = "reserva_publico_list.html"

	def get_queryset(self):
		reservas = Reserva.objects.all()

		tipoderecurso_id = self.request.GET.get('tipoderecurso_id', '')
		if tipoderecurso_id != '':
			reservas = reservas.filter(tipo_recurso_id=tipoderecurso_id)

		recurso_id = self.request.GET.get('recurso_id', '')
		if recurso_id != '':
			reservas = reservas.filter(recurso_id=recurso_id)

		solicitante_id = self.request.GET.get('solicitante_id', '')
		if solicitante_id != '':
			reservas = reservas.filter(solicitante_id=solicitante_id)


		activo = self.request.GET.get('activo', 'SI')
		if activo == 'SI':
			reservas = reservas.filter(activo=True)
		elif activo == 'NO':
			reservas = reservas.filter(activo=False)

		cancelado = self.request.GET.get('cancelado', 'NO')
		if cancelado == 'SI':
			reservas = reservas.filter(cancelado=True)
		elif cancelado == 'NO':
			reservas = reservas.filter(cancelado=False)

		entregado = self.request.GET.get('entregado', 'TODOS')
		if entregado == 'SI':
			reservas = reservas.filter(entregado=True)
		elif entregado == 'NO':
			reservas = reservas.filter(entregado=False)


		devuelto = self.request.GET.get('devuelto', 'TODOS')
		if devuelto == 'SI':
			reservas = reservas.filter(devuelto=True)
		elif devuelto == 'NO':
			reservas = reservas.filter(devuelto=False)

		return reservas.order_by('-fecha', 'hora_inicio', 'grado_prioridad_solicitante')

	"""
	def render_to_response(self, context, **response_kwargs):
		if 'excel' in self.request.GET.get('excel', ''): 
			lista_datos=[]
			datos = self.get_queryset()
			for dato in datos:
				lista_datos.append([dato.codigo, dato.nombre, dato.observaciones])

			titulos=[ 'Codigo','Nombre', 'observaciones' ]
			return listview_to_excel(lista_datos,'Reservas',titulos)
		
		return super(ReservaPublicoListView, self).render_to_response(context, **response_kwargs)
	"""

	def get_context_data(self, **kwargs):
		context = super(ReservaPublicoListView, self).get_context_data(**kwargs)

		context['tiposderecurso'] = TipoDeRecurso.objects.all()
		context['tipoderecurso_id'] = int(self.request.GET.get('tipoderecurso_id','')) if (self.request.GET.get('tipoderecurso_id','') != '') else ''

		context['recursos'] = Recurso.objects.filter(borrado=False)
		context['recurso_id'] = int(self.request.GET.get('recurso_id','')) if (self.request.GET.get('recurso_id','') != '') else ''

		context['solicitantes'] = User.objects.all()
		context['solicitante_id'] = int(self.request.GET.get('solicitante_id','')) if (self.request.GET.get('solicitante_id','') != '') else ''

		context['activo'] = self.request.GET.get('activo', 'SI')
		context['cancelado'] = self.request.GET.get('cancelado', 'NO')
		context['entregado'] = self.request.GET.get('entregado', 'TODOS')
		context['devuelto'] = self.request.GET.get('devuelto', 'TODOS')

		return context
		

class RecursoPublicoDetailView(DetailView):
	model = Recurso
	template_name = "recurso_publico_detail.html"

	def get_context_data(self, **kwargs):
		context = super(RecursoPublicoDetailView, self).get_context_data(**kwargs)
		context['detalles'] = DetalleDelRecurso.objects.filter(recurso=self.object)
		return context


class ColaRecursoPublicoDetailView(DetailView):
	model = Recurso
	template_name = "cola_recurso_publico_detail.html"

	def get_context_data(self, **kwargs):
		context = super(ColaRecursoPublicoDetailView, self).get_context_data(**kwargs)
		context['reservas'] = Reserva.objects.filter(recurso=self.object, activo=True).order_by('-fecha', 'hora_inicio', 'grado_prioridad_solicitante')

		return context

class EstadisticasRecursoPublicoDetailView(DetailView):
	model = Recurso
	template_name = "estadisticas_recurso_publico_detail.html"

	def get_context_data(self, **kwargs):
		context = super(EstadisticasRecursoPublicoDetailView, self).get_context_data(**kwargs)
		context['numero_reservas'] = Reserva.objects.filter(recurso=self.object).count()
		context['numero_mantenimientos'] = Mantenimiento.objects.filter(recurso=self.object).count()

		return context

def publico_presentacion(request):
	context = RequestContext(request)
	titulo="PORTAL PUBLICO"
	descripcion="."
	return render_to_response('admin/presentacion.html', {'titulo':titulo,'descripcion':descripcion}, context)

