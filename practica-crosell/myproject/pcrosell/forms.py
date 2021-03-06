from django import forms

largadur_choices = (('True','Larga duracion'), ('False', 'Corta duracion'))

class LargaDurForm(forms.Form):
    Duracion = forms.ChoiceField(widget=forms.Select, choices=largadur_choices)
    
    
ordenar_choices = (('fechahora', 'Fecha Ascendente'),('-fechahora', 'Fecha Descendente'),('duracion', 'Duracion Ascendente'),('-duracion', 'Duracion Descendente'),('precio', 'Precio Ascendente'),('-precio', 'Precio Descendente'),('titulo', 'Titulo Ascendente'),('-titulo', 'Titulo Descendente'),('tipo', 'Tipo Ascendente'),('-tipo', 'Tipo Descendente'))

class OrdenarForm(forms.Form):
    Ordenar = forms.ChoiceField(widget=forms.Select, choices=ordenar_choices)
    
    
tipos_choices = (('ActividadesInfantiles', 'ActividadesInfantiles'),('Circos', 'Circos'),('ComemoracionesHomenajes', 'ComemoracionesHomenajes'),('Conciertos', 'Conciertos'),('ConcursosCertamenes', 'ConcursosCertamenes'),('ConferenciasColoquios', 'ConferenciasColoquios'),('CuentacuentosTiteresMarionetas', 'CuentacuentosTiteresMarionetas'),('CursosTalleres', 'CursosTalleres'),('DanzaBallet', 'DanzaBallet'),('EspectaculosHumorMagia', 'EspectaculosHumorMagia'),('Exposiciones', 'Exposiciones'),('FeriasMuestras', 'FeriasMuestras'),('FiestasActividadesCalle', 'FiestasActividadesCalle'),('FiestasSanIsidro', 'FiestasSanIsidro'),('Flamenco', 'Flamenco'),('ItinerariosOtrasActividadesAmbientales', 'ItinerariosOtrasActividadesAmbientales'),('Jazz', 'Jazz'),('MusicaClasica', 'MusicaClasica'),('ObrasTeatro', 'ObrasTeatro'),('Opera', 'Opera'),('Peliculas', 'Peliculas'),('PerformancesEspectaculosAudiovisuales', 'PerformancesEspectaculosAudiovisuales'),('RecitalesPresentacionesActosLiterarios', 'RecitalesPresentacionesActosLiterarios'),('VisitasTuristicas', 'VisitasTuristicas'),('Zarzuelas', 'Zarzuelas'))

class TiposForm(forms.Form):
    Tipos = forms.ChoiceField(widget=forms.Select, choices=tipos_choices)
    
tamano_choices = (('13px', 'Small'), ('16px', 'Medium'), ('20px', 'Large'))
color_choices = (('black', 'Negro'), ('blue', 'Azul'), ('red', 'Rojo'), ('green', 'Verde'), ('gray', 'Gris'), ('yellow', 'Amarillo'), ('pink', 'Rosa'))
fondo_choices = (('#fff', 'Blanco'), ('#edeeae', 'Amarillo'), ('#d5f6dd', 'Verde'), ('#e4f0f6','Azul'), ('#f6e0f1','Rosa'), ('#f09c97','Rojo'), ('#c3bebe','Gris'))
banner_choices = (('Madrid3.jpg', 'Madrid1'), ('Madrid.jpg', 'Madrid2'), ('Madrid2.jpg', 'Madrid3'),('Madrid4.jpg', 'Madrid4'), ('Madrid5.png', 'Madrid5') )
    
class TituloForm (forms.Form):
    Titulo = forms.CharField(max_length = 64)

class DescripcionForm(forms.Form):
    Descripcion = forms.CharField (widget = forms.Textarea)
    
class UsuarioForm (forms.Form):
    TamanoLetra = forms.ChoiceField(widget=forms.Select, choices=tamano_choices)
    ColorLetra = forms.ChoiceField(widget=forms.Select, choices=color_choices)
    ColorFondo = forms.ChoiceField(widget=forms.Select, choices=fondo_choices)
    ImagenBanner = forms.ChoiceField(widget=forms.Select, choices=banner_choices)
    
class LoginForm (forms.Form):
    username = forms.CharField(max_length = 64)
    password = forms.CharField(max_length = 64)
    
class ComentarioForm(forms.Form):
    Comentario = forms.CharField (widget = forms.Textarea)





