from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.db.models import Q

from django.contrib.auth.models import User, Group

from reservas.models import *
from reservas.forms import *

from recursos.models import *

from extra.globals import listview_to_excel

from django.http import Http404
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from datetime import datetime	

def get_estado_recurso(recurso):
	reservas = Reserva.objects.filter(recurso_id = recurso.id, activo = True)
	if(reservas.count() > 0):
		return 1 #disponible
	return 0 #reservado

def entregar_recurso(request, pk):
	context = RequestContext(request)
	reserva = Reserva.objects.get(pk=pk)

	if reserva.recurso == None:
		return redirect('/admin/reservas/reserva/'+str(pk)+'/entregargeneral')	
	
	return redirect('/admin/reservas/reserva/'+str(pk)+'/entregarespecifico')	


class EntregarRecursoGeneralUpdateView(UpdateView):
	model = Reserva
	form_class = EntregarRecursoGeneralForm
	template_name = 'entregar_recuso_general_form.html'
	success_url= '/admin/reservas/reserva'



def entregar_recurso_especifico(request, pk):
	context = RequestContext(request)
	reserva = Reserva.objects.get(pk=pk)

	if request.method == 'POST':
		reserva.entregado = True
		reserva.fecha_hora_entrega = datetime.now()
		reserva.save()

		recurso = reserva.recurso
		recurso.estado = 3 #en uso
		recurso.save()

		return redirect('/admin/reservas/reserva')

	mensaje = "Esta seguro que desea entragar el recurso?" 

	return render_to_response("admin/confirm.html", {'mensaje': mensaje, 'object':reserva,}, context)



def recibir_recurso(request, pk):
	context = RequestContext(request)
	reserva = Reserva.objects.get(pk=pk)

	if request.method == 'POST':
		reserva.devuelto = True
		reserva.fecha_hora_devolucion = datetime.now()
		reserva.activo=False
		reserva.save()

		recurso = reserva.recurso
		recurso.estado = get_estado_recurso(recurso) # disponible o reservado
		recurso.save()

		return redirect('/admin/reservas/reserva')

	mensaje = "Esta seguro que desea recibir el recurso?" 

	return render_to_response("admin/confirm.html", {'mensaje': mensaje, 'object':reserva,}, context)


def cancelar_reserva(request, pk):
	context = RequestContext(request)
	reserva = Reserva.objects.get(pk=pk)

	if request.method == 'POST':
		reserva.cancelado = True
		reserva.fecha_hora_cancelacion = datetime.now()
		reserva.activo=False
		reserva.save()

		recurso = reserva.recurso
		if recurso != None:
			recurso.estado = get_estado_recurso(recurso) # disponible o reservado
			recurso.save()

		return redirect('/admin/reservas/reserva')

	mensaje = "Esta seguro que desea cancelar la reserva?" 

	return render_to_response("admin/confirm.html", {'mensaje': mensaje, 'object':reserva,}, context)



def cancelar_mireserva(request, pk):
	context = RequestContext(request)
	reserva = Reserva.objects.get(pk=pk)

	if request.method == 'POST':
		reserva.cancelado = True
		reserva.fecha_hora_cancelacion = datetime.now()
		reserva.activo=False
		reserva.save()

		recurso = reserva.recurso
		if recurso != None:
			recurso.estado = get_estado_recurso(recurso) # disponible o reservado
			recurso.save()

		return redirect('/admin/reservas/mireserva')

	mensaje = "Esta seguro que desea cancelar la reserva?" 

	return render_to_response("admin/confirm.html", {'mensaje': mensaje, 'object':reserva,}, context)








class ReservaListView(ListView):
	"""
	View lista de reservas, sobreescribiendo la vista propia del admin
	"""
	model = Reserva
	template_name = "reserva_list.html"

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


	def render_to_response(self, context, **response_kwargs):
		if 'excel' in self.request.GET.get('excel', ''): 
			lista_datos=[]
			datos = self.get_queryset()
			for dato in datos:
				lista_datos.append([
					dato.recurso.codigo,
					dato.recurso.nombre,
					dato.recurso.tipo.nombre,
					dato.recurso.tipo.encargado.get_full_name(),
					dato.recurso.get_estado_display(),
					dato.fecha.strftime("%d/%m/%Y"),
					dato.solicitante.get_full_name(),
					dato.get_activo_display()

				])

			titulos=[ 'Codigo','Recurso', 'Tipo de recurso', 'Encargado', 'Estado del recurso', 'fecha reserva', 'Solicitante', 'Activo' ]
			return listview_to_excel(lista_datos,'Reservas',titulos)
		
		return super(ReservaListView, self).render_to_response(context, **response_kwargs)


	def get_context_data(self, **kwargs):
		context = super(ReservaListView, self).get_context_data(**kwargs)

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
		
	@method_decorator(staff_member_required)
	def dispatch(self, *args, **kwargs):
		return super(ReservaListView, self).dispatch(*args, **kwargs)


class MiReservaListView(ListView):
	"""
	View lista de mis reservas, sobreescribiendo la vista propia del admin
	"""
	model = MiReserva
	template_name = "mireserva_list.html"

	def get_queryset(self):
		solicitante = self.request.user
		reservas = MiReserva.objects.filter(solicitante_id=solicitante.id, activo=True)

		tipoderecurso_id = self.request.GET.get('tipoderecurso_id', '')
		if tipoderecurso_id != '':
			reservas = reservas.filter(tipo_recurso_id=tipoderecurso_id)

		recurso_id = self.request.GET.get('recurso_id', '')
		if recurso_id != '':
			reservas = reservas.filter(recurso_id=recurso_id)

		print reservas

		return reservas.order_by('-fecha', 'hora_inicio', 'grado_prioridad_solicitante')


	def get_context_data(self, **kwargs):
		context = super(MiReservaListView, self).get_context_data(**kwargs)

		context['tiposderecurso'] = TipoDeRecurso.objects.all()
		context['tipoderecurso_id'] = int(self.request.GET.get('tipoderecurso_id','')) if (self.request.GET.get('tipoderecurso_id','') != '') else ''

		context['recursos'] = Recurso.objects.filter(borrado=False)
		context['recurso_id'] = int(self.request.GET.get('recurso_id','')) if (self.request.GET.get('recurso_id','') != '') else ''

		return context


@login_required
def reservas_presentacion(request):
	context = RequestContext(request)
	titulo="RESERVAS"
	descripcion="."
	return render_to_response('admin/presentacion.html', {'titulo':titulo,'descripcion':descripcion}, context)

