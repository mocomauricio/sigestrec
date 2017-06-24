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


def aprobar_mantenimiento_correctivo(request, pk):
	"""
	Establecer el estado del mantenimiento como activo=False
	"""
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


@login_required
def mantenimientos_presentacion(request):
	context = RequestContext(request)
	titulo="MANTENIMIENTOS"
	descripcion="."
	return render_to_response('admin/presentacion.html', {'titulo':titulo,'descripcion':descripcion}, context)

