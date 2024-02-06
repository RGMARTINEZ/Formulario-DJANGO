from django.db import models
from multiselectfield import MultiSelectField
from ENCUESTAS.opciones_data import *


class Encuesta(models.Model):

    autoriza_uso_informacion = models.CharField(
        '¿Usted esta de acuerdo y autoriza el uso de la información conforme a las políticas de datos de PNUD?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)
    ###  1.
    nombre_entidad_religiosa = models.CharField(
        'Nombre de la Entidad Religiosa', blank=False, null=False, max_length=255, default="")
    ###  2.
    nombre_persona = models.CharField(
        'Nombre de la persona que responde la encuesta', blank=False, null=False, max_length=255, default="")
    ###  3.
    tipo_afiliacion = models.CharField(
        'Tipo de afiliación de la persona que responde la encuesta con la entidad religiosa',
        blank=False, null=False, max_length=255, default="")
    ###  4.
    cedula = models.CharField('Cédula de la persona que responde', blank=False, null=False, max_length=50)
    ###  5.
    celular = models.CharField('Celular', blank=False, null=False, max_length=50)
    ###  6.
    correo = models.EmailField('Correo electrónico', blank=False, null=False)
    ###  7.
    celular_extra = models.CharField(
        'Si tiene otro número de celular o número fijo de contacto escríbalo aquí',
        blank=True, null=True)  # modificado
    ###  8.
    zona_entidad_religiosa = models.CharField(
        '¿En que zona se encuentra ubicada la entidad religiosa que representa?',
        blank=False, null=False, max_length=255, default="", choices=ZONAS_ENTIDADES)
    otra_zona_entidad = models.CharField(
        'Otro tipo de zona seleccionada', blank=True, null=True, max_length=255)
    ###  9.
    anos_activa_entidad = models.PositiveIntegerField(
        '¿Cuántos años lleva activa la entidad religiosa a la que representa?', blank=False, null=False)
    ###  10.
    poblacion_entidad = MultiSelectField(
        'De acuerdo con su cultura, pueblo o rasgos físicos, '
        '¿Qué población atienden y ayuda su entidad religiosa? '
        '(puede marcar varias)', blank=False, null=False, max_length=255, default="", choices=TIPO_POBLACION)
    otra_poblacion_entidad = models.CharField(
        'Otro tipo de población', blank=True, null=True, max_length=255)
    ###  11.
    grupos_personas = MultiSelectField(
        'Dentro del siguiente grupo de personas, ¿Cuál atiende y beneficia su entidad religiosa? '
        '(puede marcar varias)', blank=False, null=False, max_length=255, default="", choices=GRUPOS_PERSONAS)
    otros_grupos_personas = models.CharField(
        'Otro grupo de personas seleccionado', blank=True, null=True, max_length=255)
    ###  12.
    atiende_poblacion_discapacitada = models.CharField(
        '¿Atiende población en la entidad religiosa en condición de discapacidad?',
        blank=False, null=False, max_length=255, default="", choices=OPCIONES_SI_NO)
    ###  12.1.
    tipos_discapacidades = MultiSelectField(
        'Si respondió si en la pregunta anterior ¿Qué tipo de discapacidad '
        'tiene la población que atiende su entidad religiosa?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_CONDICION_DISCAPACIDAD)
    otra_discapacidad = models.CharField(
        'Otro discapacidad seleccionada', blank=True, null=True, max_length=255)
    ###  13.
    grupo_demografico = MultiSelectField(
        'De acuerdo a la edad, ¿Cuál es el grupo demográfico principal al que sirve su Entidad religiosa? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_EDAD)

    ###  14.    ### Partimos la pregunta en 2 para poder ser analizada mejor y solo recibir campos numericos aqui
    distribucion_hombres_entidad = models.PositiveIntegerField(
        'De acuerdo al sexo (Hombre),¿Cuál es la distribución porcentual '
        'de este en su Entidad religiosa? (ejemplo: 40% hombres)', blank=False, null=False, default=0)
    ###  14.1    
    distribucion_mujeres_entidad = models.PositiveIntegerField(
        'De acuerdo al sexo (Mujeres),¿Cuál es la distribución porcentual '
        'de este en su Entidad religiosa? (ejemplo: 60% mujeres)', blank=False, null=False, default=0)
    ###  15.
    clase_social = models.CharField(
        'De acuerdo a la clase social, ¿Cuál la principal clase '
        'que atiende su Entidad religiosa?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_CLASE_SOCIAL)
    ###  16.
    idioma_principal = MultiSelectField(
        '¿Cuál es el idioma/dialecto principal de su comunidad religiosa?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_IDIOMAS)
    otro_idioma = models.CharField(
        'Otro idioma', blank=True, null=True, max_length=255)
    ###  17.
    tipo_actividad = MultiSelectField(
        '¿Qué tipo de actividad o programas realiza su Entidad religiosa '
        'para interactuar con la comunidad en general?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)
    otra_actividad = models.CharField(
        'Otra actividad', blank=True, null=True, max_length=255)
    ###  18.
    tipo_servicios = MultiSelectField(
        '¿Qué tipo de servicios sociales ofrecen a la población local? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_TIPO_SERVICIOS)
    otro_servicio = models.CharField(
        'Otro servicio', blank=True, null=True, max_length=255)
    ###  19.
    participacion_poblacion = MultiSelectField(
        '¿Cómo se promueve la participación de la población en las actividades de su Entidad religiosa? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_PARTICIPACION_POBLACION)
    otra_participacion= models.CharField(
        'Otra participacion', blank=True, null=True, max_length=255)
    ###  20.
    colabora_proyectos_comunitarios = models.CharField(
        '¿Ha colaborado su Entidad religiosa con otras organizaciones no religiosas en proyectos comunitarios?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_COLABORA_ORGANIZACIONES)
    ###  21.
    cambio_demografia = models.CharField(
        '¿Ha notado algún cambio en la demografía o en las creencias religiosas '
        'de la población a lo largo del tiempo? Si es así, ¿cómo ha afectado esto a su Entidad religiosa?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_CAMBIO_DEMOGRAFIA)
    ###  22.
    caracter_confesinal = models.CharField(
        '¿Cuál es carácter confesional específico de su Entidad religiosa ?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_CARACTER_CONFESIONAL)
    otro_caracter_confesional = models.CharField(
        'Otro caracter confesional', blank=True, null=True, max_length=255)
    ###  22.1
    caracter_confesinal_judaimo = models.CharField(
        '¿A partir de su respuesta anterior, seleccione la que corresponde? ',
        blank=False, null=True, max_length=255, default="", choices=JUDAIMO_CHOICES)
    ###  22.2
    caracter_confesinal_islam = models.CharField(
        '¿A partir de su respuesta anterior, seleccione la que corresponde? ',
        blank=False, null=True, max_length=255, default="", choices=RAMAS_ISLAM_CHOICES)
    ###  22.3
    caracter_confesinal_cristianismo = models.CharField(
        '¿A partir de su respuesta anterior, seleccione la que corresponde? ',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_DENOMINACION_RELIGIOSA)    
    ###  22.4
    caracter_confesinal_budismo = models.CharField(
        '¿A partir de su respuesta anterior, seleccione la que corresponde? ',
        blank=False, null=True, max_length=255, default="", choices=TRADICIONES_BUDISTAS_CHOICES) 
    ###  22.5
    caracter_confesinal_hinduismo = models.CharField(
        '¿A partir de su respuesta anterior, seleccione la que corresponde? ',
        blank=False, null=True, max_length=255, default="", choices=TRADICIONES_HINDUISTAS_CHOICES)            
    ###  23
    entidad_registrada = models.CharField(
        ' ¿La Entidad religiosa está registrada en Colombia?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_REGISTRO_ENTIDAD_RELIGIOSA)
    ###  24
    tipo_vocacion = models.CharField(
        '¿Qué tipo de vocación tiene la Entidad religiosa en Colombia?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_TIPO_VOCACION)
    otra_vocacion= models.CharField(
        'Otra vocación', blank=True, null=True, max_length=255)
    ###  25
    tiene_organizaciones_sector = models.CharField(
        '¿La Entidad religiosa tiene organizaciones del sector, '
        'como fundaciones o colegios religiosos, registradas en Colombia?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_ORGANIZACIONES_REGISTRADAS)
    ###  25.1
    tiene_organizaciones_sector_nombre= models.CharField(
        'Nombre de la organización (fundaciones o colegios religiosos)', blank=False, null=True, max_length=255)
    ###  25.2
    tiene_organizaciones_sector_direccion= models.CharField(
        'Dirección (fundaciones o colegios religiosos)', blank=False, null=True, max_length=255)   
    ###  25.3
    tiene_organizaciones_sector_correo= models.CharField(
        'Correo Electrónico (fundaciones o colegios religiosos)', blank=True, null=True, max_length=255)
    ###  25.4
    tiene_organizaciones_sector_telefono= models.CharField(
        'Teléfono (fundaciones o colegios religiosos', blank=True, null=True, max_length=255)
    ###  25.5
    tiene_organizaciones_sector_nit= models.CharField(
        'NIT (fundaciones o colegios religiosos)', blank=True, null=True, max_length=255)
    ###  26
    participa_actividades_caridad= models.CharField(
        '¿La Entidad religiosa participa en actividades de caridad o '
        'servicio social en Colombia? Si es así, describa estas actividades.',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_PARTICIPACION_CARIDAD)
    
    ###  26.1
    participa_actividades_caridad_departamento= models.CharField(
        '¿En cuál departamento?', blank=False, null=True, max_length=255)
    ###  26.2
    participa_actividades_caridad_departamento_otro= models.CharField(
        '¿Qué otros departamentos tiene actividades?', blank=True, null=True, max_length=255)
    ###  26.3
    participa_actividades_carida_municipio= models.CharField(
        '¿En cuál municipio?', blank=False, null=True, max_length=255) 
    ###  26.4
    participa_actividades_carida_municipio_otro= models.CharField(
        '¿Qué otros municipios tiene actividades?', blank=True, null=True, max_length=255)
    ###  26.5
    participa_actividades_caridad_localidad= models.CharField(
        '¿En cuál localidad?', blank=True, null=True, max_length=255)
    ###  26.5
    participa_actividades_caridad_telefono= models.CharField(
        'Teléfono', blank=True, null=True, max_length=255)
    ###  26.7
    participa_actividades_caridad_descripcion= models.CharField(
        'Descríbalas', blank=True, null=True, max_length=255)

    ###  27

    colabora_proyectos_sociales = MultiSelectField(
        '¿Colabora su Entidad religiosa con otras organizaciones religiosas o no '
        'religiosas en proyectos o iniciativas sociales en Colombia?. '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_COLABORACION)
    ###  27.1
    colabora_proyectos_sociales_telefono= models.CharField(
        'Teléfono fijo', blank=True, null=True, max_length=255)
    ###  27.2
    colabora_proyectos_sociales_celular= models.CharField(
        'Celular', blank=True, null=True, max_length=255)
    ###  27.3
    colabora_proyectos_sociales_correo= models.CharField(
        'Correo electrónico de la Organización del Sector Religioso', blank=True, null=True, max_length=255)
    ###  27.4
    colabora_proyectos_sociale_representan= models.CharField(
        'Nombre del Representante Legal de la Organización del Sector Religioso', blank=False, null=True, max_length=255) 

    ###  28

    interactua_comunidad_local = MultiSelectField(
        '¿Cómo interactúa su Entidad religiosa con la comunidad local en Colombia? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_INTERACCION)
    ###  29

    ofrece_servicios_poblaciones = models.CharField(
        '¿Ofrece servicios religiosos o de apoyo a grupos específicos poblaciones '
        'dentro de la sociedad colombiana?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_SERVICIOS)
    ###  29.1
    ofrece_servicios_poblaciones_otro= models.CharField(
        '¿Cuáles son los grupos?', blank=True, null=True, max_length=255)
    ###  30

    promueve_participacion_poblacion = MultiSelectField(
        '¿Cómo promueve la participación de la población local en sus actividades? ',
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_PARTICIPACION_COMUNIDAD)
    ###  31

    impacto_comunidad_valores = models.CharField(
        '¿Ha tenido su Entidad religiosa un impacto significativo en '
        'la comunidad o la sociedad colombiana en términos '
        'de valores, ética y cultura?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_IMPACTO_COMUNIDAD)
    ###  31.1
    impacto_comunidad_valores_cuales= models.CharField(
        '¿Cuáles?', blank=True, null=True, max_length=255)
    ###  32

    lideres_participan_instancia = models.CharField(
        '¿Sus líderes y autoridades religiosas participan en alguna instancia de participación local o nacional? '
        'Si es así, por favor, especifique el tipo de instancia y su nivel de participación.',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_PARTICIPACION_LIDERES)
    ###  33

    relacionamiento_gobierno_entidad = models.CharField(
        '¿Cómo es el relacionamiento del gobierno local con la entidad religiosa?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_RELACIONAMIENTO_GOBIERNO)
    ###  34

    garantia_libertad= models.CharField(
        '¿Cómo percibe la garantía de libertad de culto en su entidad local?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_GARANTIA_LIBERTAD_CULTO)
    ###  35

    participa_proyectos_sociales= models.CharField(
        '¿La Entidad religiosa participa activamente en proyectos o programas sociales en Colombia?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_PARTICIPACION_SOCIAL)
    ###  36

    areas_temas_prioridad = MultiSelectField(
        ' ¿Qué áreas o temas sociales son prioritarios para su Entidad '
        '(por ejemplo, educación, salud, alimentación, vivienda)? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_AREAS_TEMAS)
    otra_areas_temas_prioridad= models.CharField(
        'Otra áreas', blank=True, null=True, max_length=255)

    ###  37

    principales_inciativas_sociales = MultiSelectField(
        ' ¿Cuáles son las principales iniciativas o proyectos sociales que la '
        'Entidad religiosa ha llevado a cabo en Colombia en los últimos años? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_INICIATIVAS_PROYECTOS)

    otra_principales_inciativas_sociales= models.CharField(
        'Otra iniciativas', blank=True, null=True, max_length=255)

    ###  38

    como_finacia_proyectos = MultiSelectField(
        '¿Cómo financia su Entidad religiosa sus proyectos sociales (donaciones, fondos propios, colaboraciones)? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_FINANCIAMIENTO_PROYECTOS)

    otra_como_finacia_proyectos= models.CharField(
        'Otra fuentes', blank=True, null=True, max_length=255)

    ###  39

    tiene_alianzas_ongs= models.CharField(
        '¿Tiene la Entidad religiosa alianzas con otras instituciones u '
        'ONGs para abordar temas sociales en Colombia?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_ALIANZAS)
    ###  39.1
    tiene_alianzas_ongs_cuales= models.CharField(
        '¿Cuáles?', blank=True, null=True, max_length=255)
    ###  40

    alcance_actividades_sociales = MultiSelectField(
        '¿Cuál es el alcance geográfico de las actividades sociales de su Entidad en Colombia? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_ALCANCE_GEOGRAFICO)
    ###  41

    resultados_destacados = MultiSelectField(
        '¿Cuáles son los resultados o impactos más destacados de '
        'las iniciativas sociales de su Entidad en Colombia? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_RESULTADOS_IMPACTOS)

    otros_resultados_destacados= models.CharField(
        'Otros resultados', blank=True, null=True, max_length=255)
    ###  42

    como_interactua_comunidad = MultiSelectField(
        '¿Cómo interactúa su Entidad religiosa con la comunidad local en Colombia? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_INTERACCION_COMUNIDAD)
    ###  43

    ofrece_servicios_sociedad = models.CharField(
        '¿Ofrece servicios religiosos o de apoyo a grupos específicos dentro de la sociedad colombiana?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_OFERTA_SERVICIOS)
    
    ###  43.1
    ofrece_servicios_sociedad_dificultades = MultiSelectField(
        'Ha encontrado dificultades para ejercer la participación ciudadana, como Entidades Religiosas, lo cual fue consultado por los líderes en las instancias dispuestas para tal fin por: '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_OFERTA_SERVICIOS_DIFICULTADES)
    ###  43.2
    ofrece_servicios_sociedad_tecnica = MultiSelectField(
        'hace parte de alguna mesa técnica o temática, Comité, Consejo o Red donde se discutan planes, programas y/o proyectos de interés público o general, tales como:'
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_OFERTA_SERVICIOS_TEMAS)
    ###  43.3
    ofrece_servicios_sociedad_ciudadana = MultiSelectField(
        'Ha encontrado dificultades para ejercer la participación ciudadana, como ER , en las instancias dispuestas para tal fin por:'
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_OFERTA_SERVICIOS_ER)
    ###  43.4
    ofrece_servicios_sociedad_lideres = MultiSelectField(
        ' ¿Líderes de la Entidades Religiosas han recibido capacitación en liderazgo e incidencia pública por parte de los gobiernos territoriales, gobierno nacional, ONG o empresa privada?'
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_OFERTA_SERVICIOS_LIDERES)
    ofrece_servicios_sociedad_otra= models.CharField(
        'Otra', blank=True, null=True, max_length=255)
    ###  44

    promueve_participacion_poblacion_sociales = MultiSelectField(
        '¿Cómo promueve la participación de la población local en sus actividades sociales? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_PARTICIPACION_POBLACION_SOCIALES)
    ###  45

    impacto_sociedad_valores = models.CharField(
        '¿Ha tenido su Entidad religiosa un impacto significativo en la comunidad o '
        'la sociedad colombiana en términos de valores, ética y cultura?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_IMPACTO_CULTURAL)
    ###  46

    cuantas_personas_beneficiado = models.CharField(
        'En el último año, ¿cuántas personas se han beneficiado '
        'de las actividades o proyectos de su Entidad religiosa?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_BENEFICIARIOS_ACTIVIDADES)
    ###  47

    cuales_actividades_ods = MultiSelectField(
        '¿Cuáles actividades o proyectos específicos ha llevado a cabo su organización para '
        'contribuir a la consecución de los ODS en Colombia? ' 
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_ACTIVIDADES_ODS)
    otra_cuales_actividades_ods = MultiSelectField(
        'Otras actividades relacionadas con los ODS (por favor, especifique) '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=TEMAS_CHOICES)
    ###  48

    enfoque_principal_servicios = MultiSelectField(
        '¿Cuál es el enfoque principal de su Entidad religiosa en sus actividades y servicios? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_ENFOQUE_ENTIDAD)
    otro_enfoque_principal_servicios = models.CharField(
        'Otro enfoque principal', blank=True, null=True, max_length=255)
    ###  49

    es_lider_religioso= models.CharField(
        '¿Es usted un líder religioso en su Entidad religiosa?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_SI_NO_LIDER)
    ###  50

    proporciona_seguro_lideres = models.CharField(
        '¿Su Entidad religiosa proporciona algún tipo de seguro médico o de salud para sus líderes religiosos?',
        blank=False, null=True, max_length=255, default="", choices=OPCIONES_SEGURO_MEDICO)
    ###  51

    proporciona_plan_pensiones = models.CharField(
        '¿La Entidad religiosa ofrece algún plan de jubilación o pensiones para sus líderes religiosos?',
        blank=False, null=True, max_length=255, default="", choices=PLAN_JUBILACION_CHOICES)
    ###  52

    apoyo_economico_emergencia = models.CharField(
        '¿La Entidad religiosa brinda apoyo económico o asistencia financiera a sus líderes '
        'religiosos en caso de enfermedad o emergencia?',
        blank=False, null=True, max_length=255, default="", choices=APOYO_ECONOMICO_CHOICES)
    ###  53

    proporciona_seguro_vida = models.CharField(
        '¿Su Entidad religiosa ofrece algún tipo de '
        'seguro de vida o seguro de incapacidad para sus líderes religiosos?',
        blank=False, null=True, max_length=255, default="", choices=SEGURO_VIDA_INCAPACIDAD_CHOICES)
    ###  54

    proporciona_formacion_social = models.CharField(
        '¿Se proporciona algún tipo de formación o capacitación sobre seguridad social y '
        'beneficios para líderes religiosos en su Entidad religiosa?',
        blank=False, null=True, max_length=255, default="", choices=FORMACION_SEGURIDAD_SOCIAL_CHOICES)
    ###  55

    experimentado_problema_seguridad_social = models.CharField(
        '¿Ha experimentado algún problema o desafío específico relacionado con la seguridad '
        'social o los beneficios en su papel como líder religioso?',
        blank=False, null=True, max_length=255, default="", choices=DESAFIOS_SEGURIDAD_SOCIAL_CHOICES)
    ###  56

    beneficios_implementado_seguridad = MultiSelectField(
        '¿Qué tipo de beneficios o apoyo adicional le gustaría ver implementado o mejorado en '
        'su Entidad religiosa en relación con la seguridad social? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="",
        choices=BENEFICIOS_ADICIONALES_CHOICES)

    otros_beneficios_implementado_seguridad = models.CharField(
        'Otros beneficio implementado en seguridad social', blank=True, null=True, max_length=255)
    ###  57

    participa_actividades_humanitarias = models.CharField(
        '¿La organización religiosa participa activamente en actividades humanitarias en su territorio?',
        blank=False, null=True, max_length=255, default="", choices=PARTICIPACION_HUMANITARIA_CHOICES)
    ###  58

    colabora_agencias_humanitarios = models.CharField(
        '¿Colabora su organización religiosa con agencias gubernamentales u organizaciones '
        'no religiosas en proyectos humanitarios en Colombia?',
        blank=False, null=True, max_length=255, default="", choices=ACTIVIDADES_HUMANITARIAS_CHOICES)
    ###  59

    alcance_actividades_humanitarias = models.CharField(
        '¿Cuál es el alcance geográfico de las actividades humanitarias de su organización en Colombia?',
        blank=False, null=True, max_length=255, default="", choices=ALCANCE_GEOGRAFICO_CHOICES_HUMANITARIAS)
    ###  60

    interactua_comunidad_humanitario = MultiSelectField(
        '¿¿Cómo interactúa su organización religiosa con la comunidad local en Colombia '
        'en relación con el actuar humanitario? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=INTERACCION_COMUNIDAD_CHOICES)
    ###  61

    ofrece_servicios_humanitarios = models.CharField(
        '¿Ofrece servicios humanitarios a grupos específicos dentro de la sociedad colombiana?',
        blank=False, null=True, max_length=255, default="", choices=ENFOQUE_SERVICIOS_HUMANITARIOS_CHOICES)
    ###  62

    promueve_participacion_humanitarias = MultiSelectField(
        '¿Cómo promueve la participación de la población local en sus actividades humanitarias? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=PARTICIPACION_COMUNITARIA_CHOICES)
    ###  63

    principales_desafios_humanitarios = MultiSelectField(
        '¿Cuáles son los principales desafíos que enfrenta su organización religiosa '
        'en Colombia en la actualidad en relación con su actuación humanitaria? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=DESAFIOS_CHOICES)
    ###  64

    planes_futuras_humanitarias = MultiSelectField(
        '¿Cuáles son sus planes o perspectivas futuras para continuar su labor humanitaria en Colombia? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=PLANES_PERSPECTIVAS_CHOICES)
    ###  65

    realiza_cuidados_comunidad = MultiSelectField(
        '¿Habitualmente realiza alguna de las siguientes actividades de cuidado '
        'dirigidos a otros hogares o a su comunidad? '
        '(puede seleccionar varios)',
        blank=False, null=True, max_length=255, default="", choices=ACTIVIDADES_CUIDADO_CHOICES)

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cedula

