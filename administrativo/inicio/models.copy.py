from django.db import models

class Tipoelementos(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    tabla = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tipoElementos'

class Estatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'estatus'

class Licencias(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=150, blank=True)
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg2 = models.CharField(max_length=450, blank=True)
    pathimg1 = models.CharField(max_length=450, blank=True)
    pathimg3 = models.CharField(max_length=450, blank=True)
    siglas = models.CharField(max_length=45, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'licencias'

class Pais(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=180, blank=True)
    cod = models.CharField(max_length=135, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'pais'


class Estados(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    cod = models.CharField(max_length=135, blank=True)
    pai = models.ForeignKey(Pais, null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    udpdate = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'estados'


class Municipios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    cod = models.CharField(max_length=135, blank=True)
    estado = models.ForeignKey(Estados, null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'municipios'

class Parroquias(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=360, blank=True)
    cod = models.CharField(max_length=135, blank=True)
    municipio = models.ForeignKey(Municipios, null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'parroquias'

class Fundamentos(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=135, blank=True)
    name = models.CharField(max_length=300, blank=True)
    objetivogeneral = models.CharField(max_length=900, db_column='objetivoGeneral', blank=True) # Field name made lowercase.
    introduccion = models.TextField(blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'fundamentos'


class Objetivoespecificos(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    fundamento = models.ForeignKey(Fundamentos, null=True, blank=True)
    udpdate = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'objetivoEspecificos'

class Accionesgenerales(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    objetivoespecifico = models.ForeignKey(Objetivoespecificos, null=True, db_column='objetivoEspecifico_id', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'accionesGenerales'

class Accionesespecificas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    indicador = models.CharField(max_length=600, blank=True)
    accionesgenerale = models.ForeignKey(Accionesgenerales, null=True, db_column='accionesGenerale_id', blank=True) # Field name made lowercase.
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'accionesEspecificas'

class Tipomiembros(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'tipoMiembros'

class Tipoposicions(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=150, blank=True)
    nivel = models.IntegerField(unique=True, null=True, blank=True)
    estatu_id = models.IntegerField(unique=True, null=True, blank=True)
    class Meta:
        db_table = u'tipoPosicions'

class Tipos(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    descripcion = models.CharField(max_length=900, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'tipos'


class Tipoorganizacions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'tipoOrganizacions'

class Directorios(models.Model):
    id = models.IntegerField(primary_key=True)
    documentoidentidad = models.CharField(max_length=135, db_column='documentoIdentidad', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=180, blank=True)
    apellido = models.CharField(max_length=180, blank=True)
    correo = models.CharField(max_length=360, blank=True)
    telefono1 = models.CharField(max_length=135, blank=True)
    telefono2 = models.CharField(max_length=135, blank=True)
    fax = models.CharField(max_length=135, blank=True)
    movil = models.CharField(max_length=135, blank=True)
    sector = models.CharField(max_length=360, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    parroquia = models.ForeignKey(Parroquias, null=True, blank=True)
    correobool = models.IntegerField(null=True, db_column='correoBool', blank=True) # Field name made lowercase.
    suscritobool = models.IntegerField(null=True, db_column='suscritoBool', blank=True) # Field name made lowercase.
    gruposespecie = models.CharField(max_length=600, db_column='gruposEspecie', blank=True) # Field name made lowercase.
    localidadesaccion = models.CharField(max_length=900, db_column='localidadesAccion', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'directorios'


class Actores(models.Model):
    id = models.IntegerField(primary_key=True)
    areasaccion = models.TextField(db_column='areasAccion', blank=True) # Field name made lowercase.
    ambitoaccion = models.TextField(db_column='ambitoAccion', blank=True) # Field name made lowercase.
    principalesorgfinan = models.TextField(db_column='principalesOrgFinan', blank=True) # Field name made lowercase.
    objetivos = models.TextField(blank=True)
    aniofundacion = models.DateField(null=True, db_column='anioFundacion', blank=True) # Field name made lowercase.
    telefono = models.CharField(max_length=60, blank=True)
    coordenadas = models.CharField(max_length=135, blank=True)
    rif = models.CharField(max_length=135, blank=True)
    siglas = models.CharField(max_length=135, blank=True)
    nombre = models.TextField(blank=True)
    direccion = models.TextField(blank=True)
    correo = models.CharField(max_length=600, blank=True)
    reseniahistorica = models.TextField(db_column='reseniaHistorica', blank=True) # Field name made lowercase.
    grupobio = models.TextField(db_column='grupoBio', blank=True) # Field name made lowercase.
    tipoconex = models.TextField(db_column='tipoConex', blank=True) # Field name made lowercase.
    particularidades = models.TextField(blank=True)
    actinteres = models.TextField(db_column='actInteres', blank=True) # Field name made lowercase.
    numeromiembros = models.IntegerField(null=True, db_column='numeroMiembros', blank=True) # Field name made lowercase.
    tipoorganizacion = models.ForeignKey(Tipoorganizacions, null=True, db_column='tipoOrganizacion_id', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    nombre_completo = models.CharField(max_length=600, blank=True)
    directorio = models.ForeignKey(Directorios, null=True, blank=True)
    class Meta:
        db_table = u'actores'

class Organismoadscritos(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    telefono = models.CharField(max_length=135, blank=True)
    direccion = models.CharField(max_length=900, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'organismoAdscritos'


class Actoresorganismosads(models.Model):
    actore = models.ForeignKey(Actores, null=True, blank=True)
    organismoadscrito = models.ForeignKey(Organismoadscritos, null=True, db_column='organismoAdscrito_id', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'actoresOrganismosAds'

class Areas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    datecreado = models.DateTimeField(null=True, db_column='dateCreado', blank=True) # Field name made lowercase.
    objetocreado = models.CharField(max_length=360, db_column='objetoCreado', blank=True) # Field name made lowercase.
    geomorfo = models.TextField(blank=True)
    clima = models.TextField(blank=True)
    hidrografia = models.TextField(blank=True)
    ecosistema = models.TextField(blank=True)
    altitud = models.TextField(blank=True)
    superficie = models.TextField(blank=True)
    descricion = models.TextField(blank=True)
    asentahumanos = models.TextField(db_column='asentaHumanos', blank=True) # Field name made lowercase.
    planorden = models.IntegerField(null=True, db_column='planOrden', blank=True) # Field name made lowercase.
    comollegar = models.CharField(max_length=900, db_column='comoLlegar', blank=True) # Field name made lowercase.
    concepciones = models.CharField(max_length=600, blank=True)
    siglas = models.CharField(max_length=135, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    nombrecompleto = models.CharField(max_length=600, db_column='nombreCompleto', blank=True) # Field name made lowercase.
    actore = models.ForeignKey(Actores, null=True, blank=True)
    class Meta:
        db_table = u'areas'

class Horariodetalles(models.Model):
    id = models.IntegerField(primary_key=True)
    dia = models.CharField(max_length=135, blank=True)
    horarentrada = models.TextField(db_column='horarEntrada', blank=True) # Field name made lowercase. This field type is a guess.
    horasalida = models.TextField(db_column='horaSalida', blank=True) # Field name made lowercase. This field type is a guess.
    horadescanso = models.TextField(db_column='horaDescanso', blank=True) # Field name made lowercase. This field type is a guess.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'horarioDetalles'

class Horarios(models.Model):
    horariodetalle = models.ForeignKey(Horariodetalles, null=True, db_column='horarioDetalle_id', blank=True) # Field name made lowercase.
    actore = models.ForeignKey(Actores, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'horarios'

class Areahorariodetalles(models.Model):
    area = models.ForeignKey(Areas, null=True, blank=True)
    horariodetalle = models.ForeignKey(Horariodetalles, null=True, db_column='horarioDetalle_id', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'areaHorarioDetalles'

class Bancoaudiovisuals(models.Model):
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    elemento_id = models.IntegerField(null=True, blank=True)
    directorio = models.ForeignKey(Directorios, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    clasificacion = models.CharField(max_length=360, blank=True)
    lugar = models.CharField(max_length=600, blank=True)
    descripcion = models.CharField(max_length=900, blank=True)
    tipo = models.CharField(max_length=135, blank=True)
    licencia = models.ForeignKey(Licencias, null=True, blank=True)
    observaciones = models.CharField(max_length=900, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    url = models.CharField(max_length=600, blank=True)
    class Meta:
        db_table = u'bancoAudiovisuals'

class Bibliotecas(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField(null=True, blank=True)
    autores = models.CharField(max_length=450, blank=True)
    editorial = models.CharField(max_length=600, blank=True)
    ibsn = models.CharField(max_length=135, blank=True)
    edicion = models.CharField(max_length=45, blank=True)
    numerovolumen = models.CharField(max_length=45, db_column='numeroVolumen', blank=True) # Field name made lowercase.
    resumen = models.TextField(blank=True)
    observaciones = models.CharField(max_length=900, blank=True)
    repocitorio = models.CharField(max_length=300, blank=True)
    codigolocal = models.CharField(max_length=135, db_column='codigoLocal', blank=True) # Field name made lowercase.
    elemento_id = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    autorinstitucional = models.CharField(max_length=600, db_column='autorInstitucional', blank=True) # Field name made lowercase.
    idioma = models.CharField(max_length=60, blank=True)
    numeropaginas = models.IntegerField(null=True, db_column='numeroPaginas', blank=True) # Field name made lowercase.
    aniopublicacion = models.CharField(max_length=30, db_column='anioPublicacion', blank=True) # Field name made lowercase.
    repositoriolinea = models.IntegerField(null=True, db_column='repositorioLinea', blank=True) # Field name made lowercase.
    licencia = models.ForeignKey(Licencias, null=True, blank=True)
    class Meta:
        db_table = u'bibliotecas'

class Bioregions(models.Model):
    id = models.IntegerField(primary_key=True)
    bioregion = models.CharField(max_length=600, db_column='bioRegion', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'bioRegions'

class Bioregionareas(models.Model):
    bioregion = models.ForeignKey(Bioregions, null=True, db_column='bioRegion_id', blank=True) # Field name made lowercase.
    area = models.ForeignKey(Areas, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'bioRegionAreas'



class Categorias(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=180, blank=True)
    descri = models.CharField(max_length=900, blank=True)
    vinculo = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=360, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=360, db_column='pathImgTop', blank=True) # Field name made lowercase.
    posicion = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    elemento_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'categorias'

class Imperios(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'imperios'


class Imperiomods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    dominio = models.ForeignKey(Imperios, null=True, blank=True)
    class Meta:
        db_table = u'imperioMods'

class Reinos(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    imperio = models.ForeignKey(Imperios, null=True, blank=True)
    class Meta:
        db_table = u'reinos'


class Reinomods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    imperio = models.ForeignKey(Imperios, null=True, blank=True)
    reino = models.ForeignKey(Reinos, null=True, blank=True)
    class Meta:
        db_table = u'reinoMods'


class Phylums(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    reino = models.ForeignKey(Reinos, null=True, blank=True)
    class Meta:
        db_table = u'phylums'

class Phylummods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    reino = models.ForeignKey(Reinos, null=True, blank=True)
    phylum = models.ForeignKey(Phylums, null=True, blank=True)
    class Meta:
        db_table = u'phylumMods'

class Clases(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    phylum = models.ForeignKey(Phylums, null=True, blank=True)
    class Meta:
        db_table = u'clases'


class Clasemods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    phylum = models.ForeignKey(Phylums, null=True, blank=True)
    clase = models.ForeignKey(Clases, null=True, blank=True)
    class Meta:
        db_table = u'claseMods'

class Tipocolaboradors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'tipoColaboradors'

class Ordens(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    clase = models.ForeignKey(Clases, null=True, blank=True)
    class Meta:
        db_table = u'ordens'


class Ordenmods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    clase = models.ForeignKey(Clases, null=True, blank=True)
    orden = models.ForeignKey(Ordens, null=True, blank=True)
    class Meta:
        db_table = u'ordenMods'

class Familias(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    orden = models.ForeignKey(Ordens, null=True, blank=True)
    class Meta:
        db_table = u'familias'


class Familiamods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    orden = models.ForeignKey(Ordens, null=True, blank=True)
    familia = models.ForeignKey(Familias, null=True, blank=True)
    class Meta:
        db_table = u'familiaMods'

class Generos(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    familia = models.ForeignKey(Familias, null=True, blank=True)
    class Meta:
        db_table = u'generos'


class Generomods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=600, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    familia = models.ForeignKey(Familias, null=True, blank=True)
    genero = models.ForeignKey(Generos, null=True, blank=True)
    class Meta:
        db_table = u'generoMods'





class Colaboradoresinstitutes(models.Model):
    id = models.IntegerField(primary_key=True)
    actore = models.ForeignKey(Actores, null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'colaboradoresInstitutes'

class Colaboradorespersonas(models.Model):
    tipocolaborador = models.ForeignKey(Tipocolaboradors, null=True, db_column='tipoColaborador_id', blank=True) # Field name made lowercase.
    directorio = models.ForeignKey(Directorios, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'colaboradoresPersonas'

class Tipoareaaccions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=600, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'tipoAreaAccions'

class Directoriotipoareaaccions(models.Model):
    directorio = models.ForeignKey(Directorios, null=True, blank=True)
    tipoareaaccion = models.ForeignKey(Tipoareaaccions, null=True, db_column='tipoAreaAccion_id', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'directorioTipoAreaAccions'



class Documentosasociados(models.Model):
    id = models.IntegerField(primary_key=True)
    elemento_id = models.IntegerField(null=True, blank=True)
    biblioteca = models.ForeignKey(Bibliotecas, null=True, blank=True)
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    udpdate = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'documentosAsociados'

class Documentosgenerados(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=135, blank=True)
    fecha = models.DateField(null=True, blank=True)
    elemento_id = models.IntegerField(null=True, blank=True)
    validez = models.CharField(max_length=135, blank=True)
    fechacaduc = models.DateField(null=True, db_column='fechaCaduc', blank=True) # Field name made lowercase.
    user = models.IntegerField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'documentosGenerados'

class Especies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    genero = models.ForeignKey(Generos, null=True, blank=True)
    autorespecie = models.CharField(max_length=135, db_column='autorEspecie', blank=True) # Field name made lowercase.
    nombrecomun = models.CharField(max_length=600, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcionmorfologica = models.TextField(db_column='descripcionMorfologica', blank=True) # Field name made lowercase.
    habitad = models.TextField(blank=True)
    distribucion = models.TextField(blank=True)
    habitos = models.TextField(blank=True)
    particularidades = models.TextField(blank=True)
    aspectoslegales = models.TextField(db_column='aspectosLegales', blank=True) # Field name made lowercase.
    reproduccion = models.TextField(blank=True)
    otrosnombrec = models.CharField(max_length=150, db_column='otrosNombreC', blank=True) # Field name made lowercase.
    comentariotaxonomico = models.TextField(db_column='comentarioTaxonomico', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'especies'

class Especiemods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    genero = models.ForeignKey(Generos, null=True, blank=True)
    autorespecie = models.CharField(max_length=135, db_column='autorEspecie', blank=True) # Field name made lowercase.
    nombrecomun = models.CharField(max_length=300, db_column='nombreComun', blank=True) # Field name made lowercase.
    descripcionmorfologica = models.TextField(db_column='descripcionMorfologica', blank=True) # Field name made lowercase.
    habitad = models.TextField(blank=True)
    distribucion = models.TextField(blank=True)
    habitos = models.TextField(blank=True)
    particularidades = models.TextField(blank=True)
    aspectoslegales = models.TextField(db_column='aspectosLegales', blank=True) # Field name made lowercase.
    reproduccion = models.TextField(blank=True)
    otrosnombrec = models.CharField(max_length=180, db_column='otrosNombreC', blank=True) # Field name made lowercase.
    comentariotaxonomico = models.TextField(db_column='comentarioTaxonomico', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    comentariomodific = models.CharField(max_length=300, db_column='comentarioModific', blank=True) # Field name made lowercase.
    especie = models.ForeignKey(Especies, null=True, blank=True)
    class Meta:
        db_table = u'especieMods'

class Estatuspeligros(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=135, blank=True)
    descripcion = models.TextField(blank=True)
    udpdate = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'estatusPeligros'

class Etnias(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    otrosnombre = models.CharField(max_length=600, db_column='otrosNombre', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=900, blank=True)
    distribucion = models.TextField(blank=True)
    idioma = models.TextField(blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'etnias'

class Etniaareas(models.Model):
    id = models.IntegerField(primary_key=True)
    etnia = models.ForeignKey(Etnias, null=True, blank=True)
    area = models.ForeignKey(Areas, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'etniaAreas'

class Eventos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=360, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=360, db_column='pathImgTop', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'eventos'

class Glosario(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    definicion = models.CharField(max_length=900, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'glosario'

class Modalidads(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'modalidads'

class Trabajoscongresos(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=600, blank=True)
    objetivoespecifico = models.ForeignKey(Objetivoespecificos, null=True, db_column='objetivoEspecifico_id', blank=True) # Field name made lowercase.
    modalidad = models.ForeignKey(Modalidads, null=True, blank=True)
    resumen = models.TextField(blank=True)
    evento = models.ForeignKey(Eventos, null=True, blank=True)
    class Meta:
        db_table = u'trabajosCongresos'

class Grupotrabajocongresos(models.Model):
    id = models.IntegerField(primary_key=True)
    directorio = models.ForeignKey(Directorios, null=True, blank=True)
    trabajoscongreso = models.ForeignKey(Trabajoscongresos, null=True, db_column='trabajosCongreso_id', blank=True) # Field name made lowercase.
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'grupoTrabajoCongresos'

class Grupotrabajos(models.Model):
    id = models.IntegerField(primary_key=True)
    actore = models.ForeignKey(Actores, null=True, blank=True)
    accionesespecifica = models.ForeignKey(Accionesespecificas, null=True, db_column='accionesEspecifica_id', blank=True) # Field name made lowercase.
    udpdate = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'grupoTrabajos'


class Pablabrasclaves(models.Model):
    id = models.IntegerField(primary_key=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    palabrasclave = models.CharField(max_length=135, db_column='palabrasClave', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'pablabrasClaves'


class Interconexionbibliotecas(models.Model):
    id = models.IntegerField(primary_key=True)
    elemento_id = models.IntegerField(null=True, blank=True)
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    biblioteca = models.ForeignKey(Bibliotecas, null=True, blank=True)
    class Meta:
        db_table = u'interconexionBibliotecas'

class Listarelacionpalabrasclaves(models.Model):
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    pablabrasclave = models.ForeignKey(Pablabrasclaves, null=True, db_column='pablabrasClave_id', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    elemento_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'listaRelacionPalabrasClaves'

class Manifestacionesculturales(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=300, blank=True)
    descripcion = models.TextField(blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    elemento_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'manifestacionesCulturales'

class Mapas(models.Model):
    id = models.IntegerField(primary_key=True)
    elemento_id = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=135, blank=True)
    fuente = models.CharField(max_length=600, blank=True)
    basecartogra = models.CharField(max_length=600, db_column='baseCartogra', blank=True) # Field name made lowercase.
    udpdate = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    observaciones = models.CharField(max_length=600, blank=True)
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mapas'

class Metas(models.Model):
    id = models.IntegerField(primary_key=True)
    anio = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=135, blank=True)
    accionesespecifica = models.ForeignKey(Accionesespecificas, null=True, db_column='accionesEspecifica_id', blank=True) # Field name made lowercase.
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'metas'

class Miembrosgrupotrabajos(models.Model):
    id = models.IntegerField(primary_key=True)
    tipomiembro = models.ForeignKey(Tipomiembros, null=True, db_column='tipoMiembro_id', blank=True) # Field name made lowercase.
    directorio = models.ForeignKey(Directorios, null=True, blank=True)
    grupotrabajo = models.ForeignKey(Grupotrabajos, null=True, db_column='grupoTrabajo_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'miembrosGrupoTrabajos'

class Noticias(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=135, blank=True)
    contenido = models.TextField(blank=True)
    fecha = models.DateField(null=True, blank=True)
    autor = models.CharField(max_length=135, blank=True)
    pathimg = models.CharField(max_length=360, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=360, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'noticias'

class Personalasociados(models.Model):
    directorio = models.ForeignKey(Directorios, null=True, blank=True)
    actore = models.ForeignKey(Actores, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'personalAsociados'



class PreguntasFrecuentes(models.Model):
    id = models.IntegerField(primary_key=True)
    pregunta = models.CharField(max_length=300, blank=True)
    respuesta = models.CharField(max_length=900, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    user_update = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'preguntas_frecuentes'

class Psclases(models.Model):
    id = models.IntegerField(primary_key=True)
    clase_id_id = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    status = models.CharField(max_length=150, blank=True)
    clase = models.ForeignKey(Clases, null=True, blank=True)
    tipoposicion = models.ForeignKey(Tipoposicions, null=True, db_column='tipoPosicion_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'psClases'

class Psespecies(models.Model):
    id = models.IntegerField(primary_key=True)
    especie_id_id = models.CharField(max_length=135, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    variedad = models.CharField(max_length=300, blank=True)
    tipoposicion = models.ForeignKey(Tipoposicions, null=True, db_column='tipoPosicion_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'psEspecies'

class Psfamilias(models.Model):
    id = models.IntegerField(primary_key=True)
    familia_id_id = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    familia = models.ForeignKey(Familias, null=True, blank=True)
    tipoposicion = models.ForeignKey(Tipoposicions, null=True, db_column='tipoPosicion_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'psFamilias'

class Psordens(models.Model):
    id = models.IntegerField(primary_key=True)
    orden_id_id = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    orden = models.ForeignKey(Ordens, null=True, blank=True)
    tipo_posicion = models.ForeignKey(Tipoposicions, null=True, blank=True)
    class Meta:
        db_table = u'psOrdens'

class Psphylums(models.Model):
    id = models.IntegerField(primary_key=True)
    phylum_id_id = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    tipoposicion_id = models.IntegerField(null=True, db_column='tipoPosicion_id', blank=True) # Field name made lowercase.
    phylum = models.ForeignKey(Phylums, null=True, blank=True)
    class Meta:
        db_table = u'psPhylums'

class Psreinos(models.Model):
    id = models.IntegerField(primary_key=True)
    reino_id_id = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    tipoposicion_id = models.IntegerField(null=True, db_column='tipoPosicion_id', blank=True) # Field name made lowercase.
    reino = models.ForeignKey(Reinos, null=True, blank=True)
    class Meta:
        db_table = u'psReinos'

class Reds(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=135, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'reds'

class Redessociales(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=900, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    actore = models.ForeignKey(Actores, null=True, blank=True)
    red = models.ForeignKey(Reds, null=True, blank=True)
    class Meta:
        db_table = u'redesSociales'



class Referencias(models.Model):
    id = models.IntegerField(primary_key=True)
    elemento_id = models.IntegerField(null=True, blank=True)
    paginas = models.CharField(max_length=135, blank=True)
    biblioteca = models.ForeignKey(Bibliotecas, null=True, blank=True)
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'referencias'



class Secciones(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=180, blank=True)
    descripcion = models.CharField(max_length=900, blank=True)
    pathimg = models.CharField(max_length=360, db_column='pathImg', blank=True) # Field name made lowercase.
    pathimgtop = models.CharField(max_length=360, db_column='pathImgTop', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    posicion = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'secciones'

class Servicios(models.Model):
    id = models.IntegerField(primary_key=True)
    servicios = models.CharField(max_length=135, blank=True)
    path_img = models.CharField(max_length=600, blank=True)
    class Meta:
        db_table = u'servicios'

class ServiciosArea(models.Model):
    area = models.ForeignKey(Areas, null=True, blank=True)
    servicios = models.ForeignKey(Servicios, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'servicios_area'

class Spagricolas(models.Model):
    id = models.IntegerField(primary_key=True)
    impactoagricola = models.TextField(db_column='impactoAgricola', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spAgricolas'


class Spagricolamods(models.Model):
    id = models.IntegerField(primary_key=True)
    impactoagricola = models.TextField(db_column='impactoAgricola', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    spagricola = models.ForeignKey(Spagricolas, null=True, db_column='spAgricola_id', blank=True) # Field name made lowercase.
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spAgricolaMods'

class Spaprovechables(models.Model):
    id = models.IntegerField(primary_key=True)
    usoaprovecha = models.TextField(db_column='usoAprovecha', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spAprovechables'

class Spaprovechablemods(models.Model):
    id = models.IntegerField(primary_key=True)
    usoaprovecha = models.TextField(db_column='usoAprovecha', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    spaprovechable = models.ForeignKey(Spaprovechables, null=True, db_column='spAprovechable_id', blank=True) # Field name made lowercase.
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spAprovechableMods'

class Spaprovechamientosustentables(models.Model):
    id = models.IntegerField(primary_key=True)
    usoaprovecha = models.TextField(db_column='usoAprovecha', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spAprovechamientoSustentables'

class Spaprovechamientosustentablemods(models.Model):
    id = models.IntegerField(primary_key=True)
    usoaprovecha = models.TextField(db_column='usoAprovecha', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    spaprovechamientosustentable = models.ForeignKey(Spaprovechamientosustentables, null=True, db_column='spAprovechamientoSustentable_id', blank=True) # Field name made lowercase.
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spAprovechamientoSustentableMods'

class Spendemicas(models.Model):
    id = models.IntegerField(primary_key=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    caracteristicas = models.TextField(blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spEndemicas'

class Spendemicasmods(models.Model):
    id = models.IntegerField(primary_key=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    spendemica = models.ForeignKey(Spendemicas, null=True, db_column='spEndemica_id', blank=True) # Field name made lowercase.
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spEndemicasMods'

class Spexoticas(models.Model):
    id = models.IntegerField(primary_key=True)
    impacto = models.TextField(blank=True)
    metodoinic = models.TextField(db_column='metodoInic', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    tipoexotica_id = models.IntegerField(null=True, db_column='tipoExotica_id', blank=True) # Field name made lowercase.
    especie = models.ForeignKey(Especies, null=True, blank=True)
    class Meta:
        db_table = u'spExoticas'

class Spexoticamods(models.Model):
    id = models.IntegerField(primary_key=True)
    impacto = models.TextField(blank=True)
    metodoinic = models.TextField(db_column='metodoInic', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    tipoexotica_id = models.IntegerField(null=True, db_column='tipoExotica_id', blank=True) # Field name made lowercase.
    especie = models.ForeignKey(Especies, null=True, blank=True)
    spexotica = models.ForeignKey(Spexoticas, null=True, db_column='spExotica_id', blank=True) # Field name made lowercase.
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spExoticaMods'

class Sppeligros(models.Model):
    id = models.IntegerField(primary_key=True)
    amenazas = models.TextField(blank=True)
    iniconserv = models.TextField(db_column='iniConserv', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    estatuspeligro = models.ForeignKey(Estatuspeligros, null=True, db_column='estatusPeligro_id', blank=True) # Field name made lowercase.
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spPeligros'


class Sppeligromods(models.Model):
    id = models.IntegerField(primary_key=True)
    amenazas = models.TextField(blank=True)
    iniconserv = models.TextField(db_column='iniConserv', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    sppeligro = models.ForeignKey(Sppeligros, null=True, db_column='spPeligro_id', blank=True) # Field name made lowercase.
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spPeligroMods'

class Sprepresentativaas(models.Model):
    id = models.IntegerField(primary_key=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    area = models.ForeignKey(Areas, null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'spRepresentativaAs'

class Spsaluds(models.Model):
    id = models.IntegerField(primary_key=True)
    importanciasalud = models.TextField(db_column='importanciaSalud', blank=True) # Field name made lowercase.
    metodoinic = models.TextField(db_column='metodoInic', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spSaluds'

class Spsaludtipos(models.Model):
    tipo = models.ForeignKey(Tipos, null=True, blank=True)
    spsalud = models.ForeignKey(Spsaluds, null=True, db_column='spSalud_id', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'spSaludTipos'

class Spsaludmods(models.Model):
    id = models.IntegerField(primary_key=True)
    importanciasalud = models.TextField(db_column='importanciaSalud', blank=True) # Field name made lowercase.
    metodoinic = models.TextField(db_column='metodoInic', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    spsalud = models.ForeignKey(Spsaluds, null=True, db_column='spSalud_id', blank=True) # Field name made lowercase.
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spSaludMods'

class Sptraficos(models.Model):
    id = models.IntegerField(primary_key=True)
    finestraficlic = models.TextField(db_column='finesTraficLic', blank=True) # Field name made lowercase.
    iniconserv = models.TextField(db_column='iniConserv', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spTraficos'


class Sptraficomods(models.Model):
    id = models.IntegerField(primary_key=True)
    finestraficlic = models.TextField(db_column='finesTraficLic', blank=True) # Field name made lowercase.
    iniconserv = models.TextField(db_column='iniConserv', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    sptrafico = models.ForeignKey(Sptraficos, null=True, db_column='spTrafico_id', blank=True) # Field name made lowercase.
    pathimg = models.CharField(max_length=600, db_column='pathImg', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'spTraficoMods'

class Tipoexoticas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=180, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'tipoExoticas'

class Tipoexoticacaracteristicas(models.Model):
    id = models.IntegerField(primary_key=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    especie = models.ForeignKey(Especies, null=True, blank=True)
    tipoexotica = models.ForeignKey(Tipoexoticas, null=True, db_column='tipoExotica_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tipoExoticaCaracteristicas'

class Ubicacions(models.Model):
    id = models.IntegerField(primary_key=True)
    area = models.ForeignKey(Areas, null=True, blank=True)
    parroquia = models.ForeignKey(Parroquias, null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    update = models.DateTimeField(null=True, blank=True)
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'ubicacions'

class Vinculacionactores(models.Model):
    actore = models.ForeignKey(Actores, null=True, blank=True)
    fundamento = models.ForeignKey(Fundamentos, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    update = models.DateTimeField(null=True, blank=True)
    userupdate = models.IntegerField(null=True, db_column='userUpdate', blank=True) # Field name made lowercase.
    estatu = models.ForeignKey(Estatus,null=True, blank=True)
    class Meta:
        db_table = u'vinculacionActores'

