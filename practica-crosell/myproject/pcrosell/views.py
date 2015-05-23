# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Usuario, Evento, EventosUsuario, FechaAct, Comentario, Votacion, Seguimiento
from django.http import HttpResponse, HttpResponseRedirect
import urllib
import urllib2
from datetime import datetime
import time
from BeautifulSoup import BeautifulSoup, CData
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from pcrosell.forms import LargaDurForm, OrdenarForm, TiposForm, UsuarioForm, TituloForm, LoginForm, DescripcionForm, ComentarioForm
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import logout
from django.contrib import auth

# Create your views here.

def estaautenticado (request):
    #funcion para comprobar si un usuario esta autenticado
    if request.user.is_authenticated():
        try:
            fila = Usuario.objects.get(nombre = request.user.username )
        except Usuario.DoesNotExist:
            f = Usuario (nombre = request.user.username, npag = ("Pagina de " + request.user.username))
            f.save()
        return True
    else:
        return False
        
def obtenerinfo (request, url):
    #funcion para obtener la informacion adicional de una actividad
    url = url.replace('amp;','') 
    soup = BeautifulSoup(urllib.urlopen(url).read())

    url_info = soup.find("a", {"class": "punteado"})
    if url_info is None:
        return url_info
    url_info = str(url_info)
    url_info = url_info.split('"')[3]
    url_info = "http://www.madrid.es" + url_info
    url_info = url_info.replace('amp;','') 
    soup = BeautifulSoup(urllib.urlopen(url_info).read())
    try:
        url_info = soup.find("div", {"class": "parrafo"}).string
    except AttributeError:
        url_info = soup.find("div", {"class": "parrafo"})
    
    return url_info
         
def elegiract (request, identif):
    #funcion para seleccionar una actividad
    
    autenticado =estaautenticado(request)
    
    if(autenticado):
            
            try:
                ev = Evento.objects.get(id = identif)
                try:
                    f = EventosUsuario.objects.filter(usuario__nombre = request.user.username).get(evento = ev)
                    return HttpResponse("Ese evento ya lo tienes seleccionado")
                except:
                    us = Usuario.objects.get(nombre=request.user.username)
                    fechaact = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           
                    eventoelegido = EventosUsuario (evento = ev, usuario = us, fechareg = str(fechaact))
                    eventoelegido.save()
                
            except Evento.DoesNotExist:
                return HttpResponse ("Error: identificador no valido")
          
    
    return HttpResponseRedirect("/actividad/" + identif )
    
def votar(request, identif):
    #funcion para votar una actividad
    autenticado =estaautenticado(request)

    try:
        ev = Evento.objects.get(id = identif)
        
        try: #ver si el evento ya tiene algun voto
            fila = Votacion.objects.get(evento = ev)
            puntos = fila.puntuacion + 1
            Votacion.objects.filter(evento = ev).update(puntuacion = puntos)
        except Votacion.DoesNotExist:
            puntos = 1
            Votacion(evento = ev, puntuacion = puntos).save()

        
    except Evento.DoesNotExist:
        return HttpResponse ("Error: identificador no valido")
           
    
    return HttpResponseRedirect("/actividad/" + identif )
    
    
def eliminaract (request, identif):
    #funcion para eliminar una actividad de la pag personal
    autenticado =estaautenticado(request)

    try:
        ev = Evento.objects.get(id = identif)
        
        try:
            f = EventosUsuario.objects.filter(usuario__nombre = request.user.username).get(evento = ev)
            f.delete()
        except EventosUsuario.DoesNotExist:
            return HttpResponse ("Error: el evento no se encuentra en la DDBB para poder borrarlo")
        
        
    except Evento.DoesNotExist:
        return HttpResponse ("Error: identificador no valido")
        
    return HttpResponseRedirect("/" + request.user.username )

    
def ranking (request):
    #funcion para mostrar ranking de actividades mas votadas
    autenticado = estaautenticado(request)  
    info = "RANKING DE ACTIVIDADES MAS VOTADAS"
    lista = Votacion.objects.all().order_by('-puntuacion')
    
    try:
        fila2 = Usuario.objects.get(nombre= request.user.username)
        banner = fila2.imagenbanner
        tamanoletra = fila2.tamanoletra
        colorfondo = fila2.colorfondo
        colorletra = fila2.colorletra
    except Usuario.DoesNotExist:
        banner = "Madrid3.jpg"
        tamanoletra = "13px"
        colorfondo = "#fff"
        colorletra = "black"
    
    template = get_template("index.html")
    import forms
    form_log = forms.LoginForm()
    c = Context({'lista_rank':lista,
                 'form_log': form_log,
                 'autenticado' : autenticado,
                 'nombre' : request.user.username,
                 'banner' : banner,
                 'tamanoletra': tamanoletra,
                 'colorletra': colorletra,
                 'colorfondo': colorfondo,
                 'info': info})
    rend = template.render(c)
    return HttpResponse(rend)
    
def listausuarios (request):
    #funcion para mostrar la lista de usuarios registrados
    autenticado = estaautenticado(request)  
    info = "LISTA DE USUARIOS REGISTRADOS"
    lista = Usuario.objects.all()
    
    try:
        fila2 = Usuario.objects.get(nombre= request.user.username)
        banner = fila2.imagenbanner
        tamanoletra = fila2.tamanoletra
        colorfondo = fila2.colorfondo
        colorletra = fila2.colorletra
    except Usuario.DoesNotExist:
        banner = "Madrid3.jpg"
        tamanoletra = "13px"
        colorfondo = "#fff"
        colorletra = "black"
    
    template = get_template("index.html")
    import forms
    form_log = forms.LoginForm()
    c = Context({'lista_us_reg':lista,
                 'form_log': form_log,
                 'autenticado' : autenticado,
                 'nombre' : request.user.username,
                 'banner' : banner,
                 'tamanoletra': tamanoletra,
                 'colorletra': colorletra,
                 'colorfondo': colorfondo,
                 'info': info})
    rend = template.render(c)
    return HttpResponse(rend)
    
def seguir (request, identif):
    #funcion para seguir a un usuario
    autenticado =estaautenticado(request)

    try:
        us = Usuario.objects.get(nombre = identif)
        
        try:
            fila = Seguimiento.objects.filter(usuario__nombre = request.user.username).get(usuarioseguido = us)
        except Seguimiento.DoesNotExist:
            user = Usuario.objects.get(nombre = request.user.username)
            Seguimiento(usuario = user, usuarioseguido = us).save()

        
    except Usuario.DoesNotExist:
        return HttpResponse ("Error: identificador no valido")
    
    return HttpResponseRedirect("/" + identif )
    
def dejardeseguir (request, identif):
    autenticado= estaautenticado(request)
    
    try:
        us = Usuario.objects.get(nombre = identif)
        
        try:
            fila = Seguimiento.objects.filter(usuario__nombre = request.user.username).get(usuarioseguido = us)
            fila.delete()
        except Seguimiento.DoesNotExist:
            return HttpResponse ("Error: no puede dejar de seguir a un usuario que no esta en la base de datos")
    except Usuario.DoesNotExist:
        return HttpResponse ("Error: el nombre de usurio no es valido")
        
    return HttpResponseRedirect ("/" + request.user.username)


@csrf_exempt
def todas (request):
    #funcion /todas
    info = "LISTADO DE TODOS LOS EVENTO DE MADRID"
    
    autenticado=estaautenticado(request)
        
    import datetime
        
    if request.method == "POST":
    #si recibe un post, coger el parametro necesario para ordenar la lista
    
        form_dur = LargaDurForm(request.POST)
        if form_dur.is_valid():
            modo = form_dur.cleaned_data['Duracion']
            if modo == "True":
                lista = Evento.objects.filter(largaduracion=True)
                for i in lista:
                    i.duracion = datetime.timedelta(seconds = i.duracion)
            else:
                lista = Evento.objects.filter(largaduracion=False)
                for i in lista:
                    i.duracion = datetime.timedelta(seconds = i.duracion)
                
        form_orden = OrdenarForm(request.POST)
        if form_orden.is_valid():
            modo = form_orden.cleaned_data['Ordenar']
            lista = Evento.objects.order_by(modo)
            for i in lista:
                i.duracion = datetime.timedelta(seconds = i.duracion)
            
        form_tipos = TiposForm(request.POST)
        if form_tipos.is_valid():
            modo = form_tipos.cleaned_data['Tipos']
            lista = Evento.objects.filter(tipo=modo)
            for i in lista:
                i.duracion = datetime.timedelta(seconds = i.duracion)
            
    else:
    
        lista = Evento.objects.all()
        import datetime
        for i in lista:
            i.duracion = datetime.timedelta(seconds = i.duracion)
            
              
    ult_act = ""
    n_act = ""
    if (autenticado):
        #solo si esta autenticado, mostrar recargar, ult act y num eventos
        lista_fechas = FechaAct.objects.order_by('-fecha')
        ult_act = str(lista_fechas[0].fecha)
        numacts = len(lista)
        n_act = str(numacts)
        
    try:
        fila2 = Usuario.objects.get(nombre= request.user.username)
        banner = fila2.imagenbanner
        tamanoletra = fila2.tamanoletra
        colorfondo = fila2.colorfondo
        colorletra = fila2.colorletra
    except Usuario.DoesNotExist:
        banner = "Madrid3.jpg"
        tamanoletra = "13px"
        colorfondo = "#fff"
        colorletra = "black"
        
    template = get_template("index.html")
    import forms
    form_ord = forms.OrdenarForm()
    form_tipos = forms.TiposForm()
    form_dur = forms.LargaDurForm()
    form_log = forms.LoginForm()
    c = Context({'form_ord':form_ord,
                 'form_tipos': form_tipos,
                 'form_dur' : form_dur,
                 'form_log': form_log,
                 'info': info,
                 'lista_all': lista,
                 'autenticado_all': autenticado,
                 'autenticado': autenticado,
                 'nombre' : request.user.username,
                 'todasrss' : True,
                 'banner' : banner,
                 'tamanoletra': tamanoletra,
                 'colorletra': colorletra,
                 'colorfondo': colorfondo,
                 'ult_act': ult_act,
                 'n_act': n_act})
    rend = template.render(c)
    return HttpResponse(rend)
    
    
def actualizar (request):
    #funcion para actualizar los eventos
    url = "http://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=206974-0-agenda-eventos-culturales-100&mgmtid=6c0b6d01df986410VgnVCM2000000c205a0aRCRD"
    
    soup = BeautifulSoup(urllib.urlopen(url).read())
    
    eventos = soup.findAll('contenido')
    
    for i in range(len(eventos)):
        
        titulos = eventos[i].find('atributo', {'nombre' : 'TITULO'}).string.encode('utf-8')
        try:
            tipos = eventos[i].find('atributo', {'nombre' : 'TIPO'}).string
            tipos = tipos.split('/')[3]
        except AttributeError:
            tipos = "Sin tipo"
        
        esgratis = eventos[i].find('atributo', {'nombre' : 'GRATUITO'}).string
        if esgratis == "0":
            try:
                coment_precios = eventos[i].find('atributo', {'nombre' : 'PRECIO'}).text.encode('utf-8')
                
                num_precio = coment_precios.split()
                for j in num_precio:
                    j = j.replace(',', '.')
                    try:
                        j = float(j)
                        num_precio2 = j
                        break
                    except ValueError:
                        continue                    
                
            except AttributeError:
                num_precio2 = 0
                coment_precios = "Precio desconocido"
        else:
            num_precio2 = 0
            coment_precios = "Gratis"            
        
        fechas = eventos[i].find('atributo', {'nombre' : 'FECHA-EVENTO'}).string
        fechas = datetime.strptime(fechas, '%Y-%m-%d %H:%M:%S.%f')
        
        fechasf = eventos[i].find('atributo', {'nombre' : 'FECHA-FIN-EVENTO'}).string
        fechasf = datetime.strptime(fechasf, '%Y-%m-%d %H:%M:%S.%f')
        
        
        horas = eventos[i].find('atributo', {'nombre' : 'HORA-EVENTO'}).string
        horas = str(fechas).split()[0] + " " + horas
        horas = datetime.strptime(horas, '%Y-%m-%d %H:%M')
       
        duraciones = fechasf - horas
    
        duraciones = duraciones.total_seconds()

        try:
            largadur = eventos[i].find('atributo', {'nombre' : 'EVENTO-LARGA-DURACION'}).string
        except AttributeError:
            largadur = False        
    
        if largadur == "0":
            largadur = False
        else:
            largadur = True          
        
        urls = eventos[i].find('atributo', {'nombre' : 'CONTENT-URL'}).string
        
        identif = eventos[i].find('atributo', {'nombre' : 'ID-EVENTO'}).string
        
        try:
            descrip = eventos[i].find('atributo', {'nombre' : 'DESCRIPCION'}).string.encode('utf-8')
            if descrip != " ":
                descrip = descrip
            else:
                descrip = "Sin descripcion"
        except AttributeError:
            descrip = "Sin descripcion"
                
        
        try:
            f = Evento.objects.get(identif = identif)
        except Evento.DoesNotExist:
            f = Evento (identif = identif, titulo = titulos, tipo= tipos, precio = num_precio2, comentprecio = str(coment_precios), fechahora = str(horas), duracion= duraciones, largaduracion=largadur, url=urls, descripcion=descrip)
            f.save()       
   
    fechaact = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fechaact = FechaAct(fecha = str(fechaact))
    fechaact.save()
    
    return HttpResponseRedirect("/todas")
    
def pprincipal(request):
    #funcion /

    info=( "LAS 10 ACTIVIDADES DE OCIO Y CULTURA MAS PROXIMAS")
    import datetime
    fecha_act = datetime.datetime.now()
    lista = Evento.objects.order_by('fechahora')
    lista_ev = Evento.objects.order_by('fechahora').filter(fechahora__gte = fecha_act)[:10]

    for i in lista_ev:
        i.duracion = datetime.timedelta(seconds = i.duracion)
    
    estaautenticado(request)
    autenticado = estaautenticado(request)

    lista_us = Usuario.objects.all()
     
    
    estoyeninicio = True
    try:
        fila2 = Usuario.objects.get(nombre= request.user.username)
        banner = fila2.imagenbanner
        tamanoletra = fila2.tamanoletra
        colorfondo = fila2.colorfondo
        colorletra = fila2.colorletra
    except Usuario.DoesNotExist:
        banner = "Madrid3.jpg"
        tamanoletra = "13px"
        colorfondo = "#fff"
        colorletra = "black"
    
    template = get_template("index.html")
    import forms
    form_log = forms.LoginForm()
    c = Context({'lista_ev':lista_ev,
                 'lista_us' : lista_us,
                 'form_log': form_log,
                 'autenticado' : autenticado,
                 'nombre' : request.user.username,
                 'banner' : banner,
                 'tamanoletra': tamanoletra,
                 'colorletra': colorletra,
                 'colorfondo': colorfondo,
                 'estoyeninicio': estoyeninicio,
                 'prinrss' : True,
                 'info': info})
    rend = template.render(c)
    return HttpResponse(rend)
    
@csrf_exempt    
def actividad (request, identif):   
    #funcion /actividad/id

    comentario = ""
    votos =""
    autenticado = estaautenticado(request)
    
    if request.method == "POST":
    
        if (autenticado):
            form_coment = ComentarioForm (request.POST)
            if form_coment.is_valid():
                comentario = form_coment.cleaned_data['Comentario']
                try:
                    ev = Evento.objects.get(id = identif)
                except Evento.DoesNotExist:
                    return HttpResponse ("Error: identificador no valido")
                    
                us = Usuario.objects.get(nombre = request.user.username)
                import datetime
                fechaact = datetime.datetime.now()
                com = Comentario(texto = comentario, evento = ev, usuario = us, fechacom=str(fechaact))
                com.save()
    
    
    try: 
        fila=Evento.objects.get(id=identif)
        import datetime
        fila.duracion = datetime.timedelta(seconds = fila.duracion)
        try:
            votos = Votacion.objects.get(evento__id = identif)
            votos = votos.puntuacion
            print votos
        except Votacion.DoesNotExist:
            pass
        
        #buscar la info adicional
        url2 = fila.url
        url_info = obtenerinfo (request, url2)
       
        
        if url_info is None:
            url_info = fila.descripcion
        else:
            url_info = str(url_info)
            
        fila.descripcion = url_info
     
        
    except Evento.DoesNotExist:
        return HttpResponse("Error, el identificador de actividad no es valido")
        
    try:
        fila2 = Usuario.objects.get(nombre= request.user.username)
        banner = fila2.imagenbanner
        tamanoletra = fila2.tamanoletra
        colorfondo = fila2.colorfondo
        colorletra = fila2.colorletra
    except Usuario.DoesNotExist:
        banner = "Madrid3.jpg"
        tamanoletra = "13px"
        colorfondo = "#fff"
        colorletra = "black"
        
    # c = lista de comentarios
    c = Comentario.objects.filter(evento = fila)
    
    
    template = get_template("index.html")
    import forms
    form_log = forms.LoginForm()
    form_coment = forms.ComentarioForm()
    c = Context({'info' : "Informacion de la actividad " + str(fila.id),
                'form_log': form_log,
                'autenticado': autenticado,
                'nombre' : request.user.username,
                'form_coment': form_coment,
                'banner': banner,
                'tamanoletra': tamanoletra,
                'colorletra': colorletra,
                'colorfondo': colorfondo,
                'comentario': c,
                'numcoment': len(c),
                'votos': votos,
                'fila_act' : fila})
    rend = template.render(c)
    return HttpResponse(rend)
   
@csrf_exempt
def usuario (request, nombre):
    #funcion mostrar pagina personal de usuario
    autenticado = estaautenticado(request)

    if request.method == "POST":
    
        form_titulo = TituloForm (request.POST)
        if form_titulo.is_valid():
            titulo = form_titulo.cleaned_data['Titulo']
            Usuario.objects.filter(nombre = nombre).update(npag = titulo)
        
        form_desc = DescripcionForm (request.POST)
        if form_desc.is_valid():
            descripcion = form_desc.cleaned_data['Descripcion']
            Usuario.objects.filter(nombre = nombre).update(descrpag = descripcion)
        
        form_usuario = UsuarioForm(request.POST)
        if form_usuario.is_valid(): 
            tamanoletra = form_usuario.cleaned_data['TamanoLetra']
            colorletra = form_usuario.cleaned_data['ColorLetra']
            colorfondo = form_usuario.cleaned_data['ColorFondo']
            imagenbanner = form_usuario.cleaned_data['ImagenBanner']
            Usuario.objects.filter(nombre = nombre).update(tamanoletra = tamanoletra, colorletra = colorletra, colorfondo = colorfondo, imagenbanner = imagenbanner)
                        
                
    try:
        us = Usuario.objects.get(nombre = nombre)
    except Usuario.DoesNotExist:
        return HttpResponse("Error: el usuario no existe")
    

    lista = EventosUsuario.objects.filter(usuario = us)
    fila = Usuario.objects.get(nombre= nombre)
    info = fila.npag
    descr_user = fila.descrpag
    
    lista_seg = Seguimiento.objects.filter(usuario__nombre = nombre)
    
    try:
        listacom = Comentario.objects.filter(usuario = us)
    except Comentario.DoesNotExist:
        listacom = ""
    
    try:
        fila2 = Usuario.objects.get(nombre= request.user.username)
        banner = fila2.imagenbanner
        tamanoletra = fila2.tamanoletra
        colorletra = fila2.colorletra
        colorfondo = fila2.colorfondo
    except Usuario.DoesNotExist:
        banner = "Madrid3.jpg"
        colorletra = "black"
        tamanoletra = "13px"
        colorfondo = "#fff"
        
    import datetime
    for i in lista:
        i.evento.duracion = datetime.timedelta(seconds = i.evento.duracion)

        
    template = get_template("index.html")
    import forms
    form_tit = forms.TituloForm()
    form_des = forms.DescripcionForm()
    form_us = forms.UsuarioForm()
    form_log = forms.LoginForm()
    c = Context({'form_tit':form_tit,
                 'form_des': form_des,
                 'form_us' : form_us,
                 'form_log': form_log,
                 'autenticado': autenticado,
                 'info': info,
                 'descr_user': descr_user,
                 'lista_user': lista,
                 'banner' : banner,
                 'tamanoletra': tamanoletra,
                 'colorfondo': colorfondo,
                 'nombre' : request.user.username,
                 'colorletra': colorletra,
                 'userrss' : nombre,
                 'listacom': listacom,
                 'autorcom': nombre,
                 'lista_seg': lista_seg,
                 'autenticado_us': autenticado})
    rend = template.render(c)
    return HttpResponse(rend)
    
def vercoment (request, autor):
    #funcion para mostrar comentarios
    
    info = "COMENTARIOS DE " + autor.upper()

    autenticado = estaautenticado(request)
    try:
        us = Usuario.objects.get(nombre = autor)
    except Usuario.DoesNotExist:
        return HttpResponse("Error: el usuario no existe")
    
    try:
        listacom = Comentario.objects.filter(usuario = us)
    except Comentario.DoesNotExist:
        listacom = ""
        
    try:
        fila = Usuario.objects.get(nombre= request.user.username)
        banner = fila.imagenbanner
        tamanoletra = fila.tamanoletra
        colorfondo = fila.colorfondo
        colorletra = fila.colorletra
    except Usuario.DoesNotExist:
        banner = "Madrid3.jpg"
        tamanoletra = "13px"
        colorfondo = "#fff"
        colorletra = "black"
        
    template = get_template("index.html")

    c = Context({'autenticado': autenticado,
                 'info': info,
                 'listacom': listacom,
                 'banner': banner,
                 'tamanoletra': tamanoletra,
                 'colorfondo': colorfondo,
                 'colorletra': colorletra,
                 'nombre' : request.user.username,
                 'autorcom': autor})
    rend = template.render(c)
    return HttpResponse(rend)
    
@csrf_exempt
def ayuda(request):
    #funcion para mostrar la ayuda
    autenticado = estaautenticado(request)
    
    
    p1 = "Explicacion del funcionamiento de la practica"
    p2 = "La practica se divide fundamentalmente en seis bloques."
    p3 = "El primero de ellos es la pagina principal, a la cual se accede a traves de recurso / y en la cual se muestran las diez actividades mas proximas en el tiempo y un listado de paginas personales"
    p4 = "El segundo bloque sería las paginas de usuario, a las cuales se accede con la url /id, donde id hace referencia al nombre del usuario. En esta paginas los usuarios y el resto de visitantes pueden ver las paginas seleccionadas por el propietario de la pagina. Ademas el propio usuario desde su cuenta tiene acceso a unos formularios para cambiar la apariencia de su pagina: titulo, descripcion, banner, letra... Además se ofrecera un acceso la contenido de esa misma pagina en RSS, acceso a las paginas seleccionadas, acceso a los comentarios hechos por el propietario,etc"
    p5 = "El tercero son las paginas de las distintas actividades, ubicadas en /actividad/id, donde id es el identificador unico de cada actividad. En ellas se mostrara informacion de la pagina, con una descripcion adicional, y en la parte inferior, los comentarios realizados por los diferentes usuarios"
    p6 = "El cuarto bloque sería la pagina ubicada en el recurso /todas, donde se muestran todas las actividades, y en la parte superior se ofrece la posibilidad de realizar diferentes filtrados, por titulos, duración, precio, fecha, etc, para facilitar las busquedas"
    p7 = "La quinta parte la formarían los canales RSS, uno de ellos para mostrar las paginas personales, otro para la pagina de todas las actividades y un tercero para mostrar las 10 actividades mas proximas"
    p8 = "Por ultimo la practica consta de este bloque de ayuda, para explicar brevemente el funcionamiento"
    try:
        fila = Usuario.objects.get(nombre= request.user.username)
        banner = fila.imagenbanner
        tamanoletra = fila.tamanoletra
        colorfondo = fila.colorfondo
        colorletra = fila.colorletra
    except Usuario.DoesNotExist:
        banner = "Madrid3.jpg"
        tamanoletra = "13px"
        colorfondo = "#fff"
        colorletra = "black"
        
    template = get_template("index.html")
    import forms
    form_log = forms.LoginForm()
    c = Context({'p1': p1,
                 'p2': p2,
                 'p3': p3,
                 'p4': p4,
                 'p5': p5,
                 'p6': p6,
                 'p7': p7,
                 'p8': p8,
                 'form_log': form_log,
                 'autenticado': autenticado,
                 'nombre' : request.user.username,
                 'banner': banner,
                 'tamanoletra': tamanoletra,
                 'colorfondo': colorfondo,
                 'colorletra': colorletra,
                 'info': "Ayuda"})
    rend = template.render(c)
    return HttpResponse(rend)
    

@csrf_exempt
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                   username=form.cleaned_data["username"],
                   password=form.cleaned_data["password"])
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            form = LoginForm()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def milogout (request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   
