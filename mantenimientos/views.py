from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q

from django.contrib.auth.models import User, Group

from recursos.models import *
from mantenimientos.forms import *

from extra.globals import listview_to_excel

from django.http import Http404
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

def aprobar_mantenimiento(request, pk):
	context = RequestContext(request)
	mantenimiento = Mantenimiento.objects.get(pk=pk)

	if request.method == 'POST':
		mantenimiento.activo = False
		mantenimiento.save()

		recurso = mantenimiento.recurso
		recurso.estado=0 #disponible
		recurso.save()

		return redirect('/admin/mantenimientos/mantenimiento')

	mensaje = "Esta seguro que desea aprobar el mantenimiento?" 

	return render_to_response("admin/confirm.html", {'mensaje': mensaje, 'object':mantenimiento,}, context)




class MantenimientoListView(ListView):
	"""
	View lista de mantenimientos, sobreescribiendo la vista propia del admin
	"""
	model = Mantenimiento
	template_name = "mantenimiento_list.html"

	def get_queryset(self):
		mantenimientos = Mantenimiento.objects.filter(activo=True).order_by('fecha')

		q = self.request.GET.get('q', '')
		if q != '':
			mantenimientos = mantenimientos.filter( Q(recurso__codigo__startswith=q) | Q(recurso__nombre__icontains=q) | Q(recurso__observaciones__icontains=q) )

		tipodemantenimiento = self.request.GET.get('tipodemantenimiento', '')
		if tipodemantenimiento != '':
			mantenimientos = mantenimientos.filter(tipo=int(tipodemantenimiento))

		return mantenimientos

	def render_to_response(self, context, **response_kwargs):
		if 'excel' in self.request.GET.get('excel', ''): 
			lista_datos=[]
			datos = self.get_queryset()
			for dato in datos:
				lista_datos.append([dato.recurso.nombre, dato.get_tipo_display(), dato.fecha.strftime("%Y/%m/%d")])

			titulos=[ 'Recurso','tipo ', 'fecha de mantenimiento' ]
			return listview_to_excel(lista_datos,'Mantenimientos',titulos)
		
		return super(MantenimientoListView, self).render_to_response(context, **response_kwargs)

	def get_context_data(self, **kwargs):
		context = super(MantenimientoListView, self).get_context_data(**kwargs)
		context['q'] = self.request.GET.get('q', '')
		context['tipodemantenimiento'] = self.request.GET.get('tipodemantenimiento', '')

		return context
		
	@method_decorator(staff_member_required)
	def dispatch(self, *args, **kwargs):
		return super(MantenimientoListView, self).dispatch(*args, **kwargs)


class MantenimientoAprobadoListView(MantenimientoListView):
	template_name = "mantenimiento_aprobado_list.html"

	def get_queryset(self):
		mantenimientos = Mantenimiento.objects.filter(activo=False).order_by('fecha')

		q = self.request.GET.get('q', '')
		if q != '':
			mantenimientos = mantenimientos.filter( Q(recurso__codigo__startswith=q) | Q(recurso__nombre__icontains=q) | Q(recurso__observaciones__icontains=q) )

		tipodemantenimiento = self.request.GET.get('tipodemantenimiento', '')
		if tipodemantenimiento != '':
			mantenimientos = mantenimientos.filter(tipo=int(tipodemantenimiento))

		return mantenimientos

@login_required
def mantenimientos_presentacion(request):
	context = RequestContext(request)
	titulo="MANTENIMIENTOS"
	descripcion="."
	return render_to_response('admin/presentacion.html', {'titulo':titulo,'descripcion':descripcion}, context)

