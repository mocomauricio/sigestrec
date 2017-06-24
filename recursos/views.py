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
from common.jasper import reportes
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
			print "hola"
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

		return recursos

	def render_to_response(self, context, **response_kwargs):
		if 'excel' in self.request.GET.get('excel', ''): 
			lista_datos=[]
			datos = self.get_queryset()
			for dato in datos:
				lista_datos.append([dato.codigo, dato.nombre, dato.observaciones])

			titulos=[ 'Codigo','Nombre', 'observaciones' ]
			return listview_to_excel(lista_datos,'Recursos',titulos)
		
		return super(RecursoListView, self).render_to_response(context, **response_kwargs)

	def get_context_data(self, **kwargs):
		context = super(RecursoListView, self).get_context_data(**kwargs)
		context['q'] = self.request.GET.get('q', '')
		context['tiposderecurso'] = TipoDeRecurso.objects.all()
		context['tipoderecurso_id'] = int(self.request.GET.get('tipoderecurso_id','')) if (self.request.GET.get('tipoderecurso_id','') != '') else ''
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

def marcar_como_averiado(request, pk):
	"""
	Establecer el estado del recurso como averiado=True
	"""
	context = RequestContext(request)
	recurso = Recurso.objects.get(pk=pk)
	if request.method == 'POST':
		recurso.averiado = True
		recurso.save()
		return redirect('/admin/recursos/recurso')

	mensaje = "Esta seguro que desea marcar como averiado el recurso " + recurso.nombre +"?" 

	return render_to_response("admin/confirm.html", {'mensaje': mensaje, 'object':recurso,}, context)

def marcar_como_reparado(request, pk):
	"""
	Establecer el estado del recurso como averiado=False
	"""
	context = RequestContext(request)
	recurso = Recurso.objects.get(pk=pk)
	if request.method == 'POST':
		recurso.averiado = True
		recurso.save()
		return redirect('/admin/recursos/recurso')

	mensaje = "Esta seguro que desea marcar como reparado el recurso " + recurso.nombre +"?" 

	return render_to_response("admin/confirm.html", {'mensaje': mensaje, 'object':recurso,}, context)



#class Recursoreporteview(reporteView):

#	View lista de recursos, sobreescribiendo la vista propia del admin

#	model = Recurso
#	template_name = "reporte_recursos.html"
#	 def pdf_recurso(request, pk):
#		obj = Recurso.objects.get(pk=pk)
#		reporte = "reporteDeRecursos.jasper"
#        response = HttpResponse(content_type='application/pdf')
##		response['Content-Disposition'] = 'attachment; filename="Recursos'
##			"id": pk,}))
#		return response"""
