from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.db.models import Q

from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from sistema.forms import *

from extra.globals import listview_to_excel

# Create your views here.
class UsuarioCreateView(CreateView):
	model = User
	form_class = UserCreationForm
	template_name = "usuario_form.html"

	def get_success_url(self):
		return ("/admin/auth/user/" + str(self.object.id) )


@login_required
def anular_usuario(request, pk):
	"""
	View que implementa un borrado logico de usuario seteando is_active a False y restringe eliminar cuando is_superuser == True, 
	sobreescribiendo la vista propia del admin
	"""
	context = RequestContext(request)
	usuario = User.objects.get(pk=pk)

	if usuario.is_superuser == True:
		raise Http404

	if request.method == 'POST':
		usuario.is_active = False
		usuario.save()
		return redirect('/admin/auth/user/')

	mensaje = "Esta seguro que desea dar de baja al usuario: " + (usuario.get_full_name() if usuario.get_full_name != '' else usuario.username)
	return render_to_response('admin/confirm.html', {'mensaje': mensaje}, context)

class UsuarioListView(ListView):
	"""
	View lista de usuarios, sobreescribiendo la vista propia del admin
	"""
	model = User
	template_name = "usuario_list.html"
	paginate_by = 30

	def get_queryset(self):
		usuarios = User.objects.filter(is_active=True)

		q = self.request.GET.get('q', '')
		if q != '':
			usuarios = usuarios.filter( Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(username__icontains=q) )

		return usuarios


	def render_to_response(self, context, **response_kwargs):
		if 'excel' in self.request.GET.get('excel', ''): 
			lista_datos=[]
			datos = self.get_queryset()
			for dato in datos:
				lista_datos.append([
					dato.get_full_name() if dato.get_full_name() != '' else dato.username,
					dato.email
				])

			titulos=[ 'Nombre' ,'Email']
			return listview_to_excel(lista_datos,'Usuarios',titulos)
		
		return super(UsuarioListView, self).render_to_response(context, **response_kwargs)


	def get_context_data(self, **kwargs):
		context = super(UsuarioListView, self).get_context_data(**kwargs)
		context['q'] = self.request.GET.get('q', '')
		return context

class GrupoListView(ListView):
	"""
	View lista de grupos, sobreescribiendo la vista propia del admin
	"""
	model = Group
	template_name = "grupo_list.html"
	paginate_by = 30

	def get_queryset(self):
		grupos = Group.objects.all()

		q = self.request.GET.get('q', '')
		if q != '':
			grupos = grupos.filter(name__icontains=q)

		return grupos

	def get_context_data(self, **kwargs):
		context = super(GrupoListView, self).get_context_data(**kwargs)
		context['q'] = self.request.GET.get('q', '')
		return context

def sistema_presentacion(request):
	context = RequestContext(request)
	titulo="SISTEMA"
	descripcion="."
	return render_to_response('admin/presentacion.html', {'titulo':titulo,'descripcion':descripcion}, context)
