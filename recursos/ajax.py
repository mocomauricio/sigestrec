import json

from django.http.response import HttpResponse

from recursos.models import *



def get_caracteristicas_tipo_de_recurso(request):
    id_tipoderecurso = request.GET.get('id_tipoderecurso')
    response = []
    remisiones = id_tipoderecurso.split(',')
    if id_tipoderecurso == "":
        return HttpResponse(json.dumps(response), content_type='application/json')


    caracteristicas = TipoDeRecurso.objects.get(id=id_tipoderecurso).caracteristicas.all()

    for caracteristica in caracteristicas:
        response.append({
            'id': unicode(caracteristica.id),
            'descripcion': unicode(caracteristica.descripcion)
        })

    return HttpResponse(json.dumps(response), content_type='application/json')