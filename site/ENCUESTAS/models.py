from django.db import models
from multiselectfield import MultiSelectField

TIPO_POBLACION = (
    ("INDIGENA", 'Indígena'),
    ("AFROCOLOMBIANA", 'Afrocolombiano (a)'),
    ("CAMPESINA", 'Campesino (a)'),
    ("ROM", 'Rom (Gitanos)'),
    ("RAIZAL", 'Raizal'),
    ("OTRO", 'Otro (a)'),
    ("NINGUNO", 'Ninguno (a)')
)

ZONAS_ENTIDADES = (
    ("CABECERA", 'Cabecera (Zona urbana)'),
    ("CENTRO POBALDO", 'Centro poblado, rural disperso (Zona rural)'),
    ("OTRA", 'Otra'),
)

GRUPOS_PERSONAS = [
    ('Desplazado(a)', 'Desplazado(a)'),
    ('Reincorporado(a)', 'Reincorporado(a)'),
    ('Exiliado(a)', 'Exiliado(a)'),
    ('Migrante(a)', 'Migrante(a)'),
    ('Retornado(a)', 'Retornado(a)'),
    ('Refugiado(a)', 'Refugiado(a)'),
    ('Asilado(a)', 'Asilado(a)'),
    ('Otro(a)', 'Otro(a)'),
    ('Ninguno(a)', 'Ninguno(a)'),
]

OPCIONES_CONDICION_DISCAPACIDAD = [
    ('Física o motora', 'Física o motora'),
    ('Sensorial (Sentidos)', 'Sensorial (Sentidos)'),
    ('Intelectual', 'Intelectual'),
    ('Psíquica', 'Psíquica'),
    ('Visual', 'Visual'),
    ('Múltiple', 'Múltiple'),
    ('Otra', 'Otra'),
    ('Ninguna', 'Ninguna'),
]

OPCIONES_SI_NO = [
    ('Si', 'Si'),
    ('No', 'No'),
]

OPCIONES_EDAD = [
    ('0 a 5 años', '0 a 5 años'),
    ('6 a 11 años', '6 a 11 años'),
    ('12 a 17 años', '12 a 17 años'),
    ('18 a 23 años', '18 a 23 años'),
    ('24 a 29 años', '24 a 29 años'),
    ('30 a 35 años', '30 a 35 años'),
    ('36 a 40 años', '36 a 40 años'),
    ('41 a 46 años', '41 a 46 años'),
    ('47 a 52 años', '47 a 52 años'),
    ('53 a 59 años', '53 a 59 años'),
    ('60 a 65 años', '60 a 65 años'),
    ('66 a 71 años', '66 a 71 años'),
    ('72 a 77 años', '72 a 77 años'),
    ('77 a 82 años', '77 a 82 años'),
    ('83 a 88 años', '83 a 88 años'),
    ('89 a 94 años', '89 a 94 años'),
    ('95 y más', '95 y más'),
]

OPCIONES_AUTORIZAR_USO = [
    ('SI', 'SI'),
    ('NO', 'NO'),
]

OPCIONES_CLASE_SOCIAL = [
    ('Clase alta', 'Clase alta'),
    ('Clase media', 'Clase media'),
    ('Vulnerable', 'Vulnerable'),
    ('Pobre', 'Pobre'),
]

OPCIONES_IDIOMAS = [
    ('Español', 'Español'),
    ('Inglés', 'Inglés'),
    ('Bilingüe o multilingüe', 'Bilingüe o multilingüe'),
    ('No estoy seguro/No aplicable.', 'No estoy seguro/No aplicable.'),
    ('Otro', 'Otro'),
]

OPCIONES_TIPO_ACTIVIDAD = [
    ('Servicios religiosos abiertos al público.', 'Servicios religiosos abiertos al público.'),
    ('Eventos culturales o artísticos.', 'Eventos culturales o artísticos.'),
    ('Programas de voluntariado y servicio comunitario.', 'Programas de voluntariado y servicio comunitario.'),
    ('Programas educativos o talleres.', 'Programas educativos o talleres.'),
    ('Actividades deportivas o recreativas.', 'Actividades deportivas o recreativas.'),
    ('Programas de asistencia social.', 'Programas de asistencia social.'),
    ('No realiza actividades de interacción con la comunidad en general.', 'No realiza actividades de interacción con la comunidad en general.'),
    ('Otro', 'Otro'),
]


class Encuesta(models.Model):

    autoriza_uso_informacion = models.CharField(
        '¿Usted esta de acuerdo y autoriza el uso de la información conforme a las políticas de datos de PNUD? '
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    nombre_entidad_religiosa = models.CharField(
        'Nombre de la Entidad Religiosa', blank=False, null=False, max_length=255, default="")
    nombre_persona = models.CharField(
        'Nombre de la persona que responde la encuesta', blank=False, null=False, max_length=255, default="")
    tipo_afiliacion = models.CharField(
        'Tipo de afiliación de la persona que responde la encuesta con la entidad religiosa',
        blank=False, null=False, max_length=255, default="")
    cedula = models.CharField('Cédula de la persona que responde', blank=False, null=False, max_length=50)
    celular = models.CharField('Celular', blank=False, null=False, max_length=50)
    correo = models.EmailField('Correo electrónico', blank=False, null=False)
    celular_extra = models.CharField(
        'Si tiene otro número de celular o número fijo de contacto escríbalo aquí', blank=True, null=True)  # modificado
    zona_entidad_religiosa = models.CharField(
        '¿En que zona se encuentra ubicada la entidad religiosa que representa?',
        blank=False, null=False, max_length=255, default="", choices=ZONAS_ENTIDADES)
    otra_zona_entidad = models.CharField(
        'Otro tipo de zona seleccionada', blank=True, null=True, max_length=255)
    anos_activa_entidad = models.PositiveIntegerField(
        '¿Cuántos años lleva activa la entidad religiosa a la que representa?', blank=False, null=False)

    poblacion_entidad = MultiSelectField(
        'De acuerdo con su cultura, pueblo o rasgos físicos, ¿Qué población atienden y ayuda su entidad religiosa? '
        '(puede marcar varias)', blank=False, null=False, max_length=255, default="", choices=TIPO_POBLACION)
    otra_poblacion_entidad = models.CharField(
        'Otro tipo de población seleccionado', blank=True, null=True, max_length=255)

    grupos_personas = MultiSelectField(
        'Dentro del siguiente grupo de personas, ¿Cuál atiende y beneficia su entidad religiosa? '
        '(puede marcar varias)', blank=False, null=False, max_length=255, default="", choices=GRUPOS_PERSONAS)
    otros_grupos_personas = models.CharField(
        'Otro grupo de personas seleccionado', blank=True, null=True, max_length=255)

    atiende_poblacion_discapacitada = models.CharField(
        '¿Atiende población en la entidad religiosa en condición de discapacidad?',
        blank=False, null=False, max_length=255, default=OPCIONES_SI_NO[0][0], choices=OPCIONES_SI_NO)

    tipos_discapacidades = MultiSelectField(
        'Si respondió si en la pregunta anterior ¿Qué tipo de discapacidad '
        'tiene la población que atiende su entidad religiosa?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_CONDICION_DISCAPACIDAD)

    otra_discapacidad = models.CharField(
        'Otro discapacidad seleccionada', blank=True, null=True, max_length=255)

    grupo_demografico = models.CharField(
        'De acuerdo a la edad, ¿Cuál es el grupo demográfico principal al que sirve su Entidad religiosa? '
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_EDAD)

    ### Partimos la pregunta en 2 para poder ser analizada mejor y solo recibir campos numericos aqui
    distribucion_hombres_entidad = models.PositiveIntegerField(
        'De acuerdo al sexo (Hombre),¿Cuál es la distribución porcentual '
        'de este en su Entidad religiosa? (ejemplo: 40% hombres)', blank=False, null=False, default=0)

    distribucion_mujeres_entidad = models.PositiveIntegerField(
        'De acuerdo al sexo (Mujeres),¿Cuál es la distribución porcentual '
        'de este en su Entidad religiosa? (ejemplo: 60% mujeres)', blank=False, null=False, default=0)

    clase_social = models.CharField(
        'De acuerdo a la clase social, ¿Cuál la principal clase que atiende su Entidad religiosa? (seleccione SOLO una)'
        '(puede seleccionar solo una)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_CLASE_SOCIAL)

    idioma_principal = MultiSelectField(
        '¿Cuál es el idioma/dialecto principal de su comunidad religiosa?'
        '(puede seleccionar solo una)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_IDIOMAS)

    otra_idioma = models.CharField(
        'Otro idioma', blank=True, null=True, max_length=255)

    tipo_actividad = MultiSelectField(
        '¿Qué tipo de actividad o programas realiza su Entidad religiosa para interactuar con la comunidad en general?'
        '(puede seleccionar solo una)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_actividad= models.CharField(
        'Otro actividad', blank=True, null=True, max_length=255)

    tipo_servicios = MultiSelectField(
        '¿Qué tipo de servicios sociales ofrecen a la población local?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_servicios= models.CharField(
        'Otro actividad', blank=True, null=True, max_length=255)

    participacion_poblacion = MultiSelectField(
        '¿Cómo se promueve la participación de la población en las actividades de su Entidad religiosa?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_participacion= models.CharField(
        'Otro actividad', blank=True, null=True, max_length=255)

    colabora_proyectos_comunitarios = models.CharField(
        '¿Ha colaborado su Entidad religiosa con otras organizaciones no religiosas en proyectos comunitarios?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    cambio_demografia = models.CharField(
        '¿Ha notado algún cambio en la demografía o en las creencias religiosas de la población a lo largo del tiempo? Si es así, ¿cómo ha afectado esto a su Entidad religiosa?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    caracter_confesinal = models.CharField(
        '¿Cuál es carácter confesional específico de su Entidad religiosa ?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    otra_caracter_confesional= models.CharField(
        'Otro actividad', blank=True, null=True, max_length=255)

    entidad_registrada = models.CharField(
        ' ¿La Entidad religiosa está registrada en Colombia?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    tipo_vocacion = models.CharField(
        '¿Qué tipo de vocación tiene la Entidad religiosa en Colombia?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    otra_vocacion= models.CharField(
        'Otra vocación', blank=True, null=True, max_length=255)

    tiene_organizaciones_sector = models.CharField(
        '¿La Entidad religiosa tiene organizaciones del sector, como fundaciones o colegios religiosos, registradas en Colombia?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    participa_actividades_caridad= models.CharField(
        '¿La Entidad religiosa participa en actividades de caridad o servicio social en Colombia? Si es así, describa estas actividades.',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    otros_departamentos_actividades= models.CharField(
        '¿Qué otros departamentos tiene actividades?', blank=True, null=True, max_length=255)

    otros_municipios_actividades= models.CharField(
        '¿Qué otros municipios tiene actividades?', blank=True, null=True, max_length=255)

    colabora_proyectos_sociales = MultiSelectField(
        '¿Colabora su Entidad religiosa con otras organizaciones religiosas o no '
        'religiosas en proyectos o iniciativas sociales en Colombia?.'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)


    interactua_comunidad_local = MultiSelectField(
        '¿Cómo interactúa su Entidad religiosa con la comunidad local en Colombia?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    ofrece_servicios_poblaciones = models.CharField(
        '¿Ofrece servicios religiosos o de apoyo a grupos específicos poblaciones dentro de la sociedad colombiana?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    promueve_participacion_poblacion = MultiSelectField(
        '¿Cómo promueve la participación de la población local en sus actividades?',
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    impacto_comunidad_valores = models.CharField(
        '¿Ha tenido su Entidad religiosa un impacto significativo en la comunidad o la sociedad colombiana en términos '
        'de valores, ética y cultura?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    lideres_participan_instancia = models.CharField(
        '¿Sus líderes y autoridades religiosas participan en alguna instancia de participación local o nacional? '
        'Si es así, por favor, especifique el tipo de instancia y su nivel de participación.',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    relacionamiento_gobierno_entidad = models.CharField(
        '¿Cómo es el relacionamiento del gobierno local con la entidad religiosa?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    garantia_libertad= models.CharField(
        '¿Cómo percibe la garantía de libertad de culto en su entidad local?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    participa_proyectos_sociales= models.CharField(
        '¿La Entidad religiosa participa activamente en proyectos o programas sociales en Colombia?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    areas_temas_prioridad = MultiSelectField(
        ' ¿Qué áreas o temas sociales son prioritarios para su Entidad '
        '(por ejemplo, educación, salud, alimentación, vivienda)?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_areas_temas_prioridad= models.CharField(
        'Otra áreas', blank=True, null=True, max_length=255)

    principales_inciativas_sociales = MultiSelectField(
        ' ¿Cuáles son las principales iniciativas o proyectos sociales que la '
        'Entidad religiosa ha llevado a cabo en Colombia en los últimos años?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_principales_inciativas_sociales= models.CharField(
        'Otra iniciativas', blank=True, null=True, max_length=255)

    como_finacia_proyectos = MultiSelectField(
        '¿Cómo financia su Entidad religiosa sus proyectos sociales (donaciones, fondos propios, colaboraciones)?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_como_finacia_proyectos= models.CharField(
        'Otra fuentes', blank=True, null=True, max_length=255)

    tiene_alianzas_ongs= models.CharField(
        '¿Tiene la Entidad religiosa alianzas con otras instituciones u ONGs para abordar temas sociales en Colombia?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    alcance_actividades_sociales = MultiSelectField(
        '¿Cuál es el alcance geográfico de las actividades sociales de su Entidad en Colombia?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    resultados_destacados = MultiSelectField(
        '¿Cuáles son los resultados o impactos más destacados de las iniciativas sociales de su Entidad en Colombia?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_resultados_destacados= models.CharField(
        'Otros resultados', blank=True, null=True, max_length=255)

    como_interactua_comunidad = MultiSelectField(
        '¿Cómo interactúa su Entidad religiosa con la comunidad local en Colombia?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    ofrece_servicios_sociedad = models.CharField(
        '¿Ofrece servicios religiosos o de apoyo a grupos específicos dentro de la sociedad colombiana?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    promueve_participacion_poblacion_sociales = MultiSelectField(
        '¿Cómo promueve la participación de la población local en sus actividades sociales?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    impacto_sociedad_valores = models.CharField(
        '¿Ha tenido su Entidad religiosa un impacto significativo en la comunidad o '
        'la sociedad colombiana en términos de valores, ética y cultura?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    cuantas_personas_beneficiado = models.CharField(
        'En el último año, ¿cuántas personas se han beneficiado de las actividades o proyectos de su Entidad religiosa?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    cuales_actividades_ods = MultiSelectField(
        '¿Cuáles actividades o proyectos específicos ha llevado a cabo su organización para '
        'contribuir a la consecución de los ODS en Colombia?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_cuales_actividades_ods = MultiSelectField(
        'Otras actividades relacionadas con los ODS (por favor, especifique)'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    enfoque_principal_servicios = MultiSelectField(
        '¿Cuál es el enfoque principal de su Entidad religiosa en sus actividades y servicios?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_enfoque_principal_servicios = models.CharField(
        'Otros resultados', blank=True, null=True, max_length=255)

    es_lider_religioso= models.CharField(
        '¿Es usted un líder religioso en su Entidad religiosa?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    proporciona_seguro_lideres = models.CharField(
        '¿Su Entidad religiosa proporciona algún tipo de seguro médico o de salud para sus líderes religiosos?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    proporciona_plan_pensiones = models.CharField(
        '¿La Entidad religiosa ofrece algún plan de jubilación o pensiones para sus líderes religiosos?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    apoyo_economico_emergencia = models.CharField(
        '¿La Entidad religiosa brinda apoyo económico o asistencia financiera a sus líderes '
        'religiosos en caso de enfermedad o emergencia?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    proporciona_seguro_vida = models.CharField(
        '¿Su Entidad religiosa ofrece algún tipo de seguro de vida o seguro de incapacidad para sus líderes religiosos?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    proporciona_formacion_social = models.CharField(
        '¿Se proporciona algún tipo de formación o capacitación sobre seguridad social y '
        'beneficios para líderes religiosos en su Entidad religiosa?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    experimentado_problema_seguridad_social = models.CharField(
        '¿Ha experimentado algún problema o desafío específico relacionado con la seguridad '
        'social o los beneficios en su papel como líder religioso??',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    beneficios_implementado_seguridad = MultiSelectField(
        '¿Qué tipo de beneficios o apoyo adicional le gustaría ver implementado o mejorado en '
        'su Entidad religiosa en relación con la seguridad social?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    otra_beneficios_implementado_seguridad = models.CharField(
        'Otros resultados', blank=True, null=True, max_length=255)

    participa_actividades_humanitarias = models.CharField(
        '¿La organización religiosa participa activamente en actividades humanitarias en su territorio?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    colabora_agencias_humanitarios = models.CharField(
        '¿Colabora su organización religiosa con agencias gubernamentales u organizaciones '
        'no religiosas en proyectos humanitarios en Colombia?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    alcance_actividades_humanitarias = models.CharField(
        '¿Cuál es el alcance geográfico de las actividades humanitarias de su organización en Colombia?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    interactua_comunidad_humanitario = MultiSelectField(
        '¿¿Cómo interactúa su organización religiosa con la comunidad local en Colombia '
        'en relación con el actuar humanitario?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    ofrece_servicios_humanitarios = models.CharField(
        '¿Ofrece servicios humanitarios a grupos específicos dentro de la sociedad colombiana?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_AUTORIZAR_USO)

    promueve_participacion_humanitarias = MultiSelectField(
        '¿Cómo promueve la participación de la población local en sus actividades humanitarias?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    principales_desafios_humanitarios = MultiSelectField(
        '¿Cuáles son los principales desafíos que enfrenta su organización religiosa '
        'en Colombia en la actualidad en relación con su actuación humanitaria?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    planes_futuras_humanitarias = MultiSelectField(
        '¿Cuáles son sus planes o perspectivas futuras para continuar su labor humanitaria en Colombia?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)

    realiza_cuidados_comunidad = MultiSelectField(
        '¿Habitualmente realiza alguna de las siguientes actividades de cuidado '
        'dirigidos a otros hogares o a su comunidad?'
        '(puede seleccionar varios)',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_TIPO_ACTIVIDAD)
