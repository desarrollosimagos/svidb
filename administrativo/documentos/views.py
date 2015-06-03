# -*- coding: utf8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from perfil.models import *
from menu.models import *
from plantillas.models import *
from models import *
from django.conf import settings
from administrativo.settings import  MEDIA_ROOT 

from django.db.models import Q

import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse

from congresos.models import participacioEvento,ProgramaCursos


def licencias(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None

    try:
        id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
        id_usuario = None

    try:
        id_persona = PerfilPublico.objects.get(user=id_usuario)
    except PerfilPublico.DoesNotExist:
        id_persona = None

    if id_persona == None:
       pp_id= None
    else:
       pp_id=id_persona.persona.id

    try:
        persona =  Directorios.objects.get(id=pp_id)
    except Directorios.DoesNotExist:
        persona = None

    try:
        licencia = Licencias.objects.filter()
    except Licencias.DoesNotExist:
        licencia = None
    return render_to_response('documentos/licencia.html', {'licencia':licencia,'persona':persona})


def generarPDF(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))
	
def libro_pdf(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None

    try:
        id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
        id_usuario = None

    try:
        id_persona = PerfilPublico.objects.get(user=id_usuario)
    except PerfilPublico.DoesNotExist:
        id_persona = None

    if id_persona == None:
       pp_id= None
    else:
       pp_id=id_persona.persona.id

    try:
        persona =  Directorios.objects.get(id=pp_id)
    except Directorios.DoesNotExist:
        persona = None
		
    try:
       eventos_activos = Eventos.objects.get(pk= id)
    except Eventos.DoesNotExist:
       eventos_activos = None
    d= settings.URL_SET_SITE 
    html = render_to_string('documentos/libro_pdf.html', {'pagesize':'A4', 'persona':persona,'eventos':eventos_activos,'url':d}, context_instance=RequestContext(request))
    return generarPDF(html)
	
def resumen_pdf(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None

    try:
        id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
        id_usuario = None

    try:
        id_persona = PerfilPublico.objects.get(user=id_usuario)
    except PerfilPublico.DoesNotExist:
        id_persona = None

    if id_persona == None:
       pp_id= None
    else:
       pp_id=id_persona.persona.id

    try:
        persona =  Directorios.objects.get(id=pp_id)
    except Directorios.DoesNotExist:
        persona = None
		
    try:
       trabajos = Trabajoscongresos.objects.get(pk= id)
    except Trabajoscongresos.DoesNotExist:
       trabajos = None
    today = datetime.now() #fecha actual
    dateFormat = today.strftime("%d-%m-%Y") # fecha con formato
    d= settings.URL_SET_SITE 
    # vista de ejemplo con un hipotético modelo Libro
    html = render_to_string('documentos/resumen.html', {'pagesize':'A4', 'persona':persona,'trabajos':trabajos,'url':d,'dateFormat':dateFormat}, context_instance=RequestContext(request))
    return generarPDF(html)
	
	
def previsualizarTrabajosPdf(request,id):
    _username = request.user.username
    if _username : 
       try:
           publicacion = Trabajoscongresos.objects.get(pk=id)
       except Trabajoscongresos.DoesNotExist:
           publicacion = None 
       if publicacion:
          today = datetime.now() #fecha actual
          dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
          d= settings.URL_SET_SITE 
          # vista de ejemplo con un hipotético modelo Libro
          html = render_to_string('documentos/resumenTrabajo.html', {'pagesize':'A4','publicacion':publicacion,'url':d,'dateFormat':dateFormat}, context_instance=RequestContext(request))
          return generarPDF(html)
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
	   
def previsualizarTrabajosPdf(request,id):
    _username = request.user.username
    if _username : 
       try:
           publicacion = Trabajoscongresos.objects.get(pk=id)
       except Trabajoscongresos.DoesNotExist:
           publicacion = None 
       if publicacion:
          today = datetime.now() #fecha actual
          dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
          d= settings.URL_SET_SITE 
          # vista de ejemplo con un hipotético modelo Libro
          html = render_to_string('documentos/resumenTrabajo.html', {'pagesize':'A4','publicacion':publicacion,'url':d,'dateFormat':dateFormat}, context_instance=RequestContext(request))
          return generarPDF(html)
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
	   
def ReportesCongresosTrabajos(request,id):
    _username = request.user.username
    if _username : 
       try:
           evento = Eventos.objects.get(pk=id)
       except Eventos.DoesNotExist:
           evento = None 
       if evento:
          if request.method == 'POST':
             trabajos = Trabajoscongresos.objects.filter(evento=evento)
             tematica = request.POST.get('tematica')
             modalidad = request.POST.get('modalidad')
             arbitro = request.POST.get('arbitro')
             coordi = request.POST.get('coordi')
             if tematica:
                trabajos = trabajos.filter(tematicas__id=tematica)
             if modalidad:
                trabajos = trabajos.filter(modalidad__id=modalidad)
             if arbitro:
                trabajos = trabajos.filter(trabajosarbitros__estatu=arbitro)
             if coordi:
                trabajos = trabajos.filter(estatu=coordi)

             return render_to_response("congresos/trabajos/matrix.html",{'evento':evento,'trabajos':trabajos}, context_instance=RequestContext(request))  
          else:
             return render_to_response("congresos/trabajos/matrix.html",{'evento':evento}, context_instance=RequestContext(request))       
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
	   
def ReportesCongresosCertificados(request,id):
    _username = request.user.username
    if _username : 
       try:
           evento = Eventos.objects.get(pk=id)
       except Eventos.DoesNotExist:
           evento = None 
       if evento:
          if evento.eventpadre == None:
             eventoPadre=evento.id
          else:
             eventoPadre=evento.eventpadre.id
          try:
             tipo_eventos = TipoEventos.objects.filter()
          except TipoEventos.DoesNotExist:
             tipo_eventos = None
          if request.method == 'POST':
             trabajos = Trabajoscongresos.objects.filter(Q(evento=evento) & Q(estatu=1))
             tematica = request.POST.get('tematica')
             modalidad = request.POST.get('modalidad')
             arbitro = request.POST.get('arbitro')
             coordi = request.POST.get('coordi')
             presentado = request.POST.get('presentado')
             texto = request.POST.get('txtconf')
             colet = request.POST.get('colet')

             d= settings.URL_SET_SITE 
             if tematica:
                trabajos = trabajos.filter(tematicas__id=tematica)
             if modalidad:
                trabajos = trabajos.filter(modalidad__id=modalidad)
             if arbitro:
                trabajos = trabajos.filter(trabajosarbitros__estatu=arbitro)
             if coordi:
                trabajos = trabajos.filter(estatu=coordi)
             if presentado:
                trabajos = trabajos.filter(presento=presentado)
             html = render_to_string('documentos/certificados.html', {'pagesize':'A4 landscape','trabajos':trabajos,'url':d,'MEDIA_ROOT':MEDIA_ROOT,'texto':texto,'colet':colet}, context_instance=RequestContext(request))
             return generarPDF(html) 
          else:
             return render_to_response("panel/certificado.html",{'evento':evento,'id2':id,'eventoPadre':eventoPadre,'tipo_eventos':tipo_eventos}, context_instance=RequestContext(request))       
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
	   
	   
def ReportesCongresosCertificadosTodos(request,id):
    _username = request.user.username
    if _username : 
       try:
           evento = Eventos.objects.get(pk=id)
       except Eventos.DoesNotExist:
           evento = None 
       if evento:
          if evento.eventpadre == None:
             eventoPadre=evento.id
          else:
             eventoPadre=evento.eventpadre.id
          try:
             tipo_eventos = TipoEventos.objects.filter()
          except TipoEventos.DoesNotExist:
             tipo_eventos = None
          if request.method == 'POST':
             trabajos = Trabajoscongresos.objects.filter(Q(evento=evento) & Q(estatu=1))
             tematica = request.POST.get('tematica')
             modalidad = request.POST.get('modalidad')
             arbitro = request.POST.get('arbitro')
             coordi = request.POST.get('coordi')
             presentado = request.POST.get('presentado')
             impreso = request.POST.get('impreso')
             kit = request.POST.get('kit')
             entregado = request.POST.get('entregado')
             d= settings.URL_SET_SITE 
             if tematica:
                trabajos = trabajos.filter(tematicas__id=tematica)
             if modalidad:
                trabajos = trabajos.filter(modalidad__id=modalidad)
             if arbitro:
                trabajos = trabajos.filter(trabajosarbitros__estatu=arbitro)
             if coordi:
                trabajos = trabajos.filter(estatu=coordi)
             if presentado:
                trabajos = trabajos.filter(presento=presentado)
             if impreso:
                if impreso == '0':
                   trabajos = trabajos.filter(impreso__exact=0)
                if impreso == '1':
                   trabajos = trabajos.filter(impreso__exact=1)
             if entregado:
                trabajos = trabajos.filter(entregado=entregado)
             if kit:
                trabajos = trabajos.filter(armado=kit)

             html = render_to_string('documentos/certificadosTodos.html', {'pagesize':'A4 landscape','trabajos':trabajos,'url':d,'MEDIA_ROOT':MEDIA_ROOT}, context_instance=RequestContext(request))
             return generarPDF(html) 
          else:
             return render_to_response("panel/certificado.html",{'evento':evento,'id2':id,'eventoPadre':eventoPadre,'tipo_eventos':tipo_eventos}, context_instance=RequestContext(request))       
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
	   
	   
def ReportesCongresosCertificadosPersonalizada(request,id):
    _username = request.user.username
    if _username : 
       try:
           evento = Eventos.objects.get(pk=id)
       except Eventos.DoesNotExist:
           evento = None 
       if evento:
          if request.method == 'POST':
             cedula = request.POST.get('cedula')
             nombre = request.POST.get('nombre')
             titulo = request.POST.get('titulo')
             modalidad = request.POST.get('modalidad')
             coatores = request.POST.get('coatores')
             d= settings.URL_SET_SITE 
             html = render_to_string('documentos/certificadosperso.html', {'pagesize':'A4 landscape','url':d,'MEDIA_ROOT':MEDIA_ROOT,'cedula':cedula,'nombre':nombre,'titulo':titulo,'modalidad':modalidad,'coatores':coatores}, context_instance=RequestContext(request))
             return generarPDF(html) 
          else:
             return render_to_response("panel/certificadoperso.html",{'evento':evento,'id2':id}, context_instance=RequestContext(request))       
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
	   
def ReportesCongresosCertificadosParticipacion(request,id,per):
    _username = request.user.username
    if _username : 
       try:
           evento = Eventos.objects.get(pk=id)
       except Eventos.DoesNotExist:
           evento = None 
       try:
           persona =  Directorios.objects.get(id=per)
       except Directorios.DoesNotExist:
           persona = None
       if evento:
#           titulo = evento.titulo
           cedula = persona.documentoidentidad
           nombre = persona.nombre
           apellido = persona.apellido
           d= settings.URL_SET_SITE 
           html = render_to_string('documentos/certificadospartici.html', {'pagesize':'A4 landscape','url':d,'MEDIA_ROOT':MEDIA_ROOT,'cedula':cedula,'nombre':nombre,'apellido':apellido,'evento':evento,'persona':persona,'titulo':""}, context_instance=RequestContext(request))            
           return generarPDF(html) 
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
	   
def ReportesCongresosCertificadosSeleccion(request,id,id2):
    _username = request.user.username
    d= settings.URL_SET_SITE 
    if _username : 
       try:
           trabajos = Trabajoscongresos.objects.get(pk=id)
       except Eventos.DoesNotExist:
           trabajos = None 
       try:
           persona =  Directorios.objects.get(id=id2)
       except Directorios.DoesNotExist:
           persona = None
       if trabajos:
          html = render_to_string('documentos/certificadosTrabajosSolo.html', {'pagesize':'A4 landscape','trabajos':trabajos,'url':d,'MEDIA_ROOT':MEDIA_ROOT,'persona':persona,'imprimirTodo':None}, context_instance=RequestContext(request))
          return generarPDF(html)     
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
	   
def ReportesCongresosCertificadosSeleccionTodos(request,id):
    _username = request.user.username
    d= settings.URL_SET_SITE 
    if _username : 
       try:
           trabajos = Trabajoscongresos.objects.get(pk=id)
       except Eventos.DoesNotExist:
           trabajos = None 
       if trabajos:
          html = render_to_string('documentos/certificadosTrabajosTodos.html', {'pagesize':'A4 landscape','trabajos':trabajos,'url':d,'MEDIA_ROOT':MEDIA_ROOT,'imprimirTodo':True}, context_instance=RequestContext(request))
          return generarPDF(html)     
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
	   
def EventosMasivosPDF(request,id):
    _username = request.user.username
    d= settings.URL_SET_SITE 
    if _username : 
       try:
           participantes = participacioEvento.objects.filter(Q(evento__id=id) & Q(estatu=3))
       except participacioEvento.DoesNotExist:
           participantes = None 
       if participantes:
          try:
              programa = ProgramaCursos.objects.get(evento__id=id)
          except ProgramaCursos.DoesNotExist:
              programa = None 
          html = render_to_string('documentos/masivoevento.html', {'pagesize':'A4 landscape','participantes':participantes,'url':d,'MEDIA_ROOT':MEDIA_ROOT,'imprimirTodo':True,'programa':programa}, context_instance=RequestContext(request))
          return generarPDF(html)     
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")
