# -*- coding: utf-8 -*-
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
#from reportlab.lib.pagesizes import letter, LEGAL, landscape
from reportlab.lib.pagesizes import A4

from reportlab.platypus import Table
from io import BytesIO
from reportlab.lib.units import mm

from django.http.response import HttpResponse
from datetime import datetime

from reservas.models import *
from extra.globals import separador_de_miles

def reporte_entrega_recurso(request, pk):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "informe_de_entrega_"+ datetime.now().strftime('%Y-%m-%d|%H:%M:%S') + '.pdf'

    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name.replace(" ","_")
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=(A4),
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )

    reserva = Reserva.objects.get(pk=pk)

    reporte = []
    styles = getSampleStyleSheet()


    linea = Paragraph("Comprobante de entrega de recurso", styles['Title'])
    reporte.append(linea)


    mensaje = "Entrega del recurso " + reserva.recurso.nombre + " (cod.: " + reserva.recurso.codigo + ") fecha "
    mensaje = mensaje + reserva.fecha_hora_entrega.strftime('%d/%m/%Y %H:%M:%S') + " al usuario " + reserva.solicitante.get_full_name()
    mensaje = mensaje + " segun reserva Nro.: " + str(reserva.id)
    linea = Paragraph(mensaje, styles['Normal'])
    reporte.append(linea)


    t = Table([
        ("", "",),
        ("", "",),
        ("........................", "......................",),
        ("firma del encargado","firma del solicitante",),
    ])
    t.setStyle(TableStyle(
        [
            #('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            #('GRID', (0, 0), (-1, -1), 1, colors.black),
             ('ALIGN',(0,0),(-1,0),'CENTER'),
            # ('ALIGN',(2,1),(2,-1),'RIGHT'),
            # ('ALIGN',(4,1),(4,-1),'RIGHT'),
        ]
    ))

    reporte.append(t)



    doc.build(reporte)
    response.write(buff.getvalue())
    buff.close()
    return response

def reporte_devolucion_recurso(request, pk):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "informe_de_devolucion_"+ datetime.now().strftime('%Y-%m-%d|%H:%M:%S') + '.pdf'

    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name.replace(" ","_")
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=(A4),
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )

    reserva = Reserva.objects.get(pk=pk)

    reporte = []
    styles = getSampleStyleSheet()


    linea = Paragraph("Comprobante de devolucion de recurso", styles['Title'])
    reporte.append(linea)


    mensaje = "devolucion del recurso " + reserva.recurso.nombre + " (cod.: " + reserva.recurso.codigo + ") fecha "
    mensaje = mensaje + reserva.fecha_hora_devolucion.strftime('%d/%m/%Y %H:%M:%S') + " al usuario " + reserva.solicitante.get_full_name()
    mensaje = mensaje + " segun reserva Nro.: " + str(reserva.id)
    linea = Paragraph(mensaje, styles['Normal'])
    reporte.append(linea)


    t = Table([
        ("", "",),
        ("", "",),
        ("........................", "......................",),
        ("firma del encargado","firma del solicitante",),
    ])
    t.setStyle(TableStyle(
        [
            #('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            #('GRID', (0, 0), (-1, -1), 1, colors.black),
             ('ALIGN',(0,0),(-1,0),'CENTER'),
            # ('ALIGN',(2,1),(2,-1),'RIGHT'),
            # ('ALIGN',(4,1),(4,-1),'RIGHT'),
        ]
    ))

    reporte.append(t)



    doc.build(reporte)
    response.write(buff.getvalue())
    buff.close()
    return response

