#######################################################
    """
    
    titulos = soup.findAll('atributo', {'nombre' : 'TITULO'})
   
    
    
    for i in range(len(titulos)):
        
        salida += str(titulos[i].string.encode('utf-8')) + "<br/>"
       
    

   
    #titulo= titulo.encode('utf-8')
    
    tipos = soup.findAll('atributo', {'nombre' : 'TIPO'})
    
    for i in range(len(tipos)):
        salida += str(tipos[i].string) + "<br/>"
    
    
    esgratis = soup.findAll('atributo', {'nombre' : 'GRATUITO'})
    for i in range(len(esgratis)):
        if esgratis == "0":
        
            precios = soup.findAll('atributo', {'nombre' : 'PRECIO'})
            for i in range(len(precios)):
                salida += str(precios[i].string)
        else:
            salida += "Gratuito" + "<br/>"
    
    
    
    fecha = soup.find('atributo', {'nombre' : 'FECHA-EVENTO'}).string
    fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S.%f')
    
    fechaf = soup.find('atributo', {'nombre' : 'FECHA-FIN-EVENTO'}).string
    fechaf = datetime.strptime(fechaf, '%Y-%m-%d %H:%M:%S.%f')
    
    hora = soup.find('atributo', {'nombre' : 'HORA-EVENTO'}).string
    hora = str(fecha).split()[0] + " " + hora
    hora = datetime.strptime(hora, '%Y-%m-%d %H:%M')
    
    duracion = fechaf - hora
    
    duracion = duracion.total_seconds()
    
    largadur = soup.find('atributo', {'nombre' : 'EVENTO-LARGA-DURACION'}).string
    
    if largadur == "0":
        largadur = False
    else:
        largadur = True
        
    
    url = soup.find('atributo', {'nombre' : 'CONTENT-URL'}).string
    
    try:
        f = Evento.objects.get(titulo = titulo)
    except Evento.DoesNotExist:
        f = Evento (titulo = titulo, tipo= tipo, precio = precio, fechahora = str(hora), duracion= str(duracion), largaduracion=largadur, url=url)
        f.save()
    
   
    
    salida = str(titulo) + "</br>" + str(tipo) + "</br>"+ str(precio) + "</br>" + str(fecha) + "</br>" + str(fechaf)  + "</br>" + str(duracion) + "</br>" + str(hora) + "</br>" + str(largadur) + "</br>" + str(url)
    
    """
