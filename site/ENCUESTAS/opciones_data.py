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

OPCIONES_TIPO_SERVICIOS = [
    ('Asistencia alimentaria (por ejemplo, bancos de alimentos).',
     'Asistencia alimentaria (por ejemplo, bancos de alimentos).'),
    ('Refugio o vivienda temporal para personas sin hogar.', 'Refugio o vivienda temporal para personas sin hogar.'),
    ('Apoyo psicológico o de salud mental.', 'Apoyo psicológico o de salud mental.'),
    ('Programas de apoyo a familias en situación de vulnerabilidad.',
     'Programas de apoyo a familias en situación de vulnerabilidad.'),
    ('Ayuda financiera o asesoramiento económico.', 'Ayuda financiera o asesoramiento económico.'),
    ('Servicios de atención médica o clínicas de salud.', 'Servicios de atención médica o clínicas de salud.'),
    ('Programas de educación para adultos.', 'Programas de educación para adultos.'),
    ('Programas de inclusión y apoyo a inmigrantes y refugiados.',
     'Programas de inclusión y apoyo a inmigrantes y refugiados.'),
    ('Apoyo espiritual para el sector penitenciario y carcelario.',
     'Apoyo espiritual para el sector penitenciario y carcelario.'),
    ('NO_OFRECEMOS_SERVICIOS', 'No ofrecemos servicios sociales.'),
    ('OTRO', 'Otro'),
]

OPCIONES_PARTICIPACION_POBLACION = [
    ('INVITACIONES_Y_COMUNICACIONES', 'A través de invitaciones y comunicaciones regulares a los miembros.'),
    ('EVENTOS_Y_ACTIVIDADES', 'Mediante la organización de eventos y actividades atractivas.'),
    ('PARTICIPACION_EN_DECISIONES', 'Fomentando la participación activa en la toma de decisiones.'),
    ('VOLUNTARIADO_Y_SERVICIO_COMUNITARIO', 'Ofreciendo oportunidades de voluntariado y servicio comunitario.'),
    ('GRUPOS_Y_COMITES', 'Facilitando la formación de grupos y comités de interés.'),
    ('APOYO_AL_DESARROLLO_DE_TALENTOS', 'Brindando apoyo y recursos para el desarrollo de talentos y habilidades.'),
    ('PLATAFORMAS_EN_LINEA_REDES_SOCIALES', 'Utilizando plataformas en línea o redes sociales para la comunicación.'),
    ('NO_PROMUEVE_PARTICIPACION', 'No se promueve activamente la participación de la población.'),
    ('OTRO', 'Otro'),
]


OPCIONES_COLABORA_ORGANIZACIONES = [
    ('COLABORACION_VARIOS_PROYECTOS',
     'Sí, hemos colaborado en varios proyectos comunitarios con organizaciones no religiosas.'),
    ('COLABORACION_ALGUNOS_PROYECTOS',
     'Sí, hemos colaborado en algunos proyectos comunitarios con organizaciones no religiosas.'),
    ('NO_COLABORACION_ORGANIZACIONES_NO_RELIGIOSAS',
     'No, no hemos colaborado con organizaciones no religiosas en proyectos comunitarios.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]

###  21.
OPCIONES_CAMBIO_DEMOGRAFIA = [
    ('CAMBIOS_NOTADOS',
     'Sí, hemos notado cambios en la demografía y las creencias '
     'religiosas de la población a lo largo del tiempo. ¿Cuáles?'),
    ('SIN_CAMBIOS_SIGNIFICATIVOS',
     'No, no hemos notado cambios significativos en la demografía o las creencias religiosas de la población.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]

###  22.
OPCIONES_CARACTER_CONFESIONAL = [
    ('JUDAISMO', 'Judaísmo'),
    ('ISLAM', 'Islam'),
    ('CRISTIANISMO', 'Cristianismo'),
    ('BUDISMO', 'Budismo'),
    ('HINDUISMO', 'Hinduismo'),
    ('OTRO', 'Otro'),
]

###  22.1

JUDAIMO_CHOICES = [
    ('ASQUENAZIES', 'Asquenazíes'),
    ('SEFARDIES', 'Sefardíes'),
]

###  22.2

RAMAS_ISLAM_CHOICES = [
    ('SUNITAS', 'Sunitas'),
    ('CHIITAS', 'Chiitas'),
]

###  22.3

OPCIONES_DENOMINACION_RELIGIOSA = [
    ('CATOLICA_ROMANA', 'Católica Romana'),
    ('PRESBITERIANAS', 'Presbiterianas'),
    ('CATOLICA_ORTODOXA', 'Católica Ortodoxa'),
    ('PENTECOSTALES_TRINITARIAS', 'Pentecostales Trinitarias'),
    ('CATOLICA_ANGLICANA', 'Católica Anglicana'),
    ('PENTECOSTALES_UNITARIAS', 'Pentecostales Unitarias'),
    ('CATOLICA_LUTERANA', 'Católica Luterana'),
    ('CARISMATICAS', 'Carismáticas'),
    ('BAUTISTAS', 'Bautistas'),
    ('ADVENTISTAS', 'Adventistas'),
    ('MENONITAS', 'Menonitas'),
    ('MORMONES', 'Mormones'),
    ('METODISTAS', 'Metodistas'),
    ('TESTIGOS_DE_JEHOVA', 'Testigos de Jehová'),
    ('OTRA', 'Otra'),
]

###  22.4

TRADICIONES_BUDISTAS_CHOICES = [
    ('TIBETANO', 'Tibetano'),
    ('SOTO_ZEN', 'Soto Zen'),
    ]

###  22.5

TRADICIONES_HINDUISTAS_CHOICES = [
    ('VISNUISMO', 'Visnuismo'),
    ('KRISNAISMO', 'Krisnaísmo'),
    ('SHIVAISMO', 'Shivaísmo'),
]


###  23.
OPCIONES_REGISTRO_ENTIDAD_RELIGIOSA = [
    ('REGISTRADA_SI', 'Sí, la Entidad religiosa está registrada en Colombia.'),
    ('REGISTRADA_NO', 'No, la Entidad religiosa no está registrada en Colombia.'),
    ('REGISTRADA_TRANSITO', 'No, pero está en tránsito'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]

###  24
OPCIONES_TIPO_VOCACION = [
    ('IGLESIA', 'Iglesia'),
    ('CONFESIONAL', 'Confesional'),
    ('DENOMINACION', 'Denominación'),
    ('ASOCIACIONES_PASTORES', 'Asociaciones de pastores'),
    ('FEDERACION_O_CONFEDERACION', 'Federación o confederación'),
    ('OTRA', 'Otra (por favor especifique)'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),

]

###  25
OPCIONES_ORGANIZACIONES_REGISTRADAS = [
    ('ORGANIZACIONES_REGISTRADAS_SI', 'Sí, tiene organizaciones del sector registradas.'),
    ('ORGANIZACIONES_REGISTRADAS_NO', 'No, no tiene organizaciones del sector registradas.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]

###  26
OPCIONES_PARTICIPACION_CARIDAD = [
    ('PARTICIPACION_SI', 'Sí, participamos en actividades de caridad y servicio social.'),
    ('PARTICIPACION_NO', 'No, no participamos en actividades de caridad o servicio social.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  27
OPCIONES_COLABORACION = [
    ('COLABORACION_RELIGIOSAS', 'Sí, colaboramos con otras organizaciones religiosas en proyectos o iniciativas.'),
    ('COLABORACION_NO_RELIGIOSAS', 'Sí, colaboramos con organizaciones no religiosas en proyectos o iniciativas.'),
    ('NO_COLABORACION', 'No, no colaboramos con otras organizaciones '
                        'religiosas o no religiosas en proyectos o iniciativas.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]

###  28

OPCIONES_INTERACCION = [
    ('SERVICIOS_RELIGIOSOS', 'A través de servicios religiosos y actividades abiertas al público.'),
    ('EVENTOS_CULTURALES', 'Organizando eventos culturales o artísticos para la comunidad.'),
    ('VOLUNTARIADO_COMUNITARIO', 'Fomentando programas de voluntariado y servicio comunitario.'),
    ('PROGRAMAS_EDUCATIVOS', 'Ofreciendo programas educativos o talleres para la comunidad.'),
    ('ACTIVIDADES_DEPORTIVAS', 'Promoviendo actividades deportivas o recreativas para todos.'),
    ('ASISTENCIA_SOCIAL', 'Realizando programas de asistencia social para quienes lo necesitan.'),
    ('PLATAFORMAS_EN_LINEA', 'Utilizando plataformas en línea o redes sociales para interactuar con la comunidad.'),
    ('NO_INTERACCION', 'No interactuamos activamente con la comunidad local.'),
]
###  29

OPCIONES_SERVICIOS = [
    ('SERVICIOS_SI', 'Sí, ofrecemos servicios religiosos o de apoyo a grupos específicos (abrir a cuáles).'),
    ('SERVICIOS_NO', 'No, no ofrecemos servicios religiosos o de apoyo a grupos específicos.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  30

OPCIONES_PARTICIPACION_COMUNIDAD = [
    ('INVITACIONES_COMUNIDAD', 'A través de invitaciones y comunicaciones regulares a los miembros de la comunidad.'),
    ('EVENTOS_ATRACTIVOS', 'Organizando eventos y actividades atractivas para la participación.'),
    ('TOMA_DECISIONES_PARTICIPATIVA', 'Fomentando la toma de decisiones '
                                      'participativa en la planificación de actividades.'),
    ('VOLUNTARIADO_COMUNITARIO_OPCIONES', 'Ofreciendo oportunidades de voluntariado y servicio comunitario.'),
    ('FORMACION_GRUPOS_COMITES', 'Facilitando la formación de grupos y comités de interés.'),
    ('APOYO_RECURSOS_TALENTOS', 'Brindando apoyo y recursos para el desarrollo de talentos '
                                'y habilidades de la comunidad.'),
    ('PLATAFORMAS_EN_LINEA_COMUNICACION', 'Utilizando plataformas en línea o '
                                          'redes sociales para la comunicación y participación.'),
    ('NO_PROMOVEMOS', 'No promovemos activamente la participación de la población local en nuestras actividades.'),
]
###  31

OPCIONES_IMPACTO_COMUNIDAD = [
    ('IMPACTO_SI', 'Sí'),
    ('IMPACTO_NO', 'No'),
    ('NO_APLICA', 'No aplica'),
]
###  32

OPCIONES_PARTICIPACION_LIDERES = [
    ('PARTICIPACION_LOCAL', 'Sí, nuestros líderes participan activamente en instancias locales de participación, '
                            'como consejos de vecinos o juntas de acción comunal.'),
    ('PARTICIPACION_LOCAL_NACIONAL', 'Sí, nuestros líderes participan en instancias '
                                     'locales y nacionales de participación, como comités ciudadanos o asambleas.'),
    ('PARTICIPACION_NACIONAL', 'Sí, nuestros líderes participan en instancias '
                               'nacionales de participación, como organizaciones religiosas a '
                               'nivel nacional o coaliciones interreligiosas.'),
    ('NO_PARTICIPACION', 'No, nuestros líderes no participan en instancias de participación local o nacional.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  33

OPCIONES_RELACIONAMIENTO_GOBIERNO = [
    ('RELACION_POSITIVA', 'El gobierno local mantiene una relación positiva y colaborativa con la entidad religiosa.'),
    ('RELACION_NEUTRAL', 'El gobierno local tiene una relación neutral con '
                         'la entidad religiosa, sin interacciones significativas.'),
    ('RELACION_TENSA', 'El gobierno local tiene una relación tensa o conflictiva con la entidad religiosa.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  34

OPCIONES_GARANTIA_LIBERTAD_CULTO = [
    ('GARANTIA_PLENAMENTE', 'La entidad local garantiza plenamente la libertad de culto y religión.'),
    ('GARANTIA_CIERTAS', 'La entidad local ofrece ciertas garantías, pero podría mejorar en este aspecto.'),
    ('RESTRICCIONES_SIGNIFICATIVAS', 'La entidad local presenta restricciones significativas '
                                     'a la libertad de culto y religión.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  35

OPCIONES_PARTICIPACION_SOCIAL = [
    ('PARTICIPACION_ACTIVAMENTE', 'Sí, participamos activamente en proyectos y programas sociales en Colombia.'),
    ('NO_PARTICIPACION_SOCIAL', 'No, no participamos en proyectos ni programas sociales en Colombia.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  36

OPCIONES_AREAS_TEMAS = [
    ('EDUCACION', 'Educación'),
    ('SALUD', 'Salud'),
    ('ALIMENTACION', 'Alimentación'),
    ('VIVIENDA', 'Vivienda'),
    ('POBREZA', 'Pobreza'),
    ('OTROS', 'Otros'),
    ('NO_PRIORITARIOS', 'No tenemos áreas o temas sociales prioritarios.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  37


OPCIONES_INICIATIVAS_PROYECTOS = [
    ('PROYECTOS_EDUCATIVOS', 'Proyectos educativos.'),
    ('PROGRAMAS_SALUD', 'Programas de salud y atención médica.'),
    ('INICIATIVAS_ALIMENTACION', 'Iniciativas de alimentación para comunidades necesitadas.'),
    ('PROGRAMAS_VIVIENDA', 'Programas de vivienda para población vulnerable.'),
    ('APOYO_NINOS_JOVENES', 'Actividades de apoyo a niños y jóvenes en riesgo.'),
    ('PROYECTOS_COMUNITARIOS', 'Proyectos de desarrollo comunitario.'),
    ('OTRAS_INICIATIVAS', 'Otros'),
    ('NO_LLEVADO_A_CABO', 'No hemos llevado a cabo iniciativas o proyectos sociales en Colombia en los últimos años.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  38


OPCIONES_FINANCIAMIENTO_PROYECTOS = [
    ('DONACIONES_MIEMBROS', 'Principalmente a través de donaciones de miembros y feligreses.'),
    ('FONDOS_PROPIOS', 'Usando fondos propios de la Entidad religiosa.'),
    ('COLABORACIONES_ORGANIZACIONES', 'Colaborando con otras organizaciones o entidades para obtener financiamiento.'),
    ('DONACIONES_EMPRESAS', 'Recibiendo donaciones de empresas u organizaciones externas.'),
    ('SUBVENCIONES_GOBIERNO', 'Apoyándose en subvenciones gubernamentales o de instituciones internacionales.'),
    ('OTRAS_FUENTES', 'Otras fuentes de financiamiento (por favor, especifique).'),
    ('NO_FINANCIAMOS', 'No financiamos proyectos sociales.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  39

OPCIONES_ALIANZAS = [
    ('ALIANZAS_SI', 'Sí, tenemos alianzas con otras instituciones u ONGs para abordar temas sociales.'),
    ('ALIANZAS_NO', 'No, no tenemos alianzas con otras instituciones u ONGs para abordar temas sociales.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  40

OPCIONES_ALCANCE_GEOGRAFICO = [
    ('LOCAL', 'Local, centrado en una comunidad o barrio específico.'),
    ('MUNICIPAL', 'Municipal, abarcando varias comunidades o barrios en un municipio.'),
    ('DEPARTAMENTAL', 'Departamental, extendiéndose a lo largo de un departamento o región.'),
    ('NACIONAL', 'Nacional, cubriendo múltiples departamentos en todo el país.'),
    ('INTERNACIONAL', 'Internacional, llevando a cabo actividades sociales a nivel internacional.'),
    ('NO_ACTIVIDADES_SOCIALES', 'No realizamos actividades sociales en Colombia.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  41

OPCIONES_RESULTADOS_IMPACTOS = [
    ('MEJORA_EDUCACION', 'Mejora en la educación de la comunidad.'),
    ('ACCESO_SERVICIOS_SALUD', 'Mayor acceso a servicios de salud.'),
    ('REDUCCION_MALNUTRICION', 'Reducción de la malnutrición.'),
    ('INCREMENTO_CALIDAD_VIDA', 'Incremento en la calidad de vida de comunidades vulnerables.'),
    ('APOYO_POBLACIONES_RIESGO', 'Apoyo a poblaciones en situación de riesgo.'),
    ('FORTALECIMIENTO_COHESION_COMUNITARIA', 'Fortalecimiento de la cohesión comunitaria.'),
    ('OTRAS_MEJORAS_SOCIALES', 'Otras mejoras sociales (por favor, especifique).'),
    ('NO_ACTIVIDADES_SOCIALES', 'No hemos realizado iniciativas sociales en Colombia.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  42

OPCIONES_INTERACCION_COMUNIDAD = [
    ('SERVICIOS_RELIGIOSOS', 'A través de servicios religiosos y actividades abiertas al público.'),
    ('EVENTOS_CULTURALES', 'Organizando eventos y actividades culturales para la comunidad.'),
    ('VOLUNTARIADO_SERVICIO_COMUNITARIO', 'Fomentando programas de voluntariado y servicio comunitario.'),
    ('PROGRAMAS_EDUCATIVOS_TALLERES', 'Ofreciendo programas educativos o talleres para la comunidad.'),
    ('ACTIVIDADES_DEPORTIVAS_RECREATIVAS', 'Promoviendo actividades deportivas o recreativas para todos.'),
    ('ASISTENCIA_SOCIAL', 'Realizando programas de asistencia social para quienes lo necesitan.'),
    ('PLATAFORMAS_EN_LINEA_REDES_SOCIALES', 'Utilizando plataformas en línea o '
                                            'redes sociales para interactuar con la comunidad.'),
    ('NO_INTERACCION', 'No interactuamos activamente con la comunidad local.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  43

OPCIONES_OFERTA_SERVICIOS = [
    ('SERVICIOS_ESPECIFICOS', 'Sí, ofrecemos servicios religiosos o de apoyo a grupos '
                              'específicos, como niños, jóvenes o personas mayores. ¿Cuáles?'),
    ('ABIERTO_TODA_COMUNIDAD', 'No, nuestros servicios religiosos son abiertos a toda '
                               'la comunidad sin distinción de grupos específicos.'),
    ('NO_OFRECE_SERVICIOS', 'No ofrecemos servicios religiosos en Colombia.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]

###  43.1

OPCIONES_OFERTA_SERVICIOS_DIFICULTADES = [
    ('RUIDO_CON_VECINOS', 'Diferencias con vecinos por ruido.'),
    ('DANIOS_FISICOS_BIENES_ER', 'Daños físicos a los bienes de la ER'),
    ('CONTROVERSIAS_PARQUEO', 'Controversias por zonas de parqueo para fieles/asociados.'),
    ('DOMICILIO_ER', 'Dificultad para establecer el domicilio de su ER'),
    ('DISCRIMINACION_INTOLERANCIA_RELIGIOSA', 'Discriminación o intolerancia religiosa.'),
    ('SIN_DIFICULTADES', 'No se han encontrado dificultades'),
]

###  43.2

OPCIONES_OFERTA_SERVICIOS_TEMAS = [
    ('EDUCACION', 'Educación'),
    ('DISCAPACIDAD', 'Discapacidad'),
    ('ACCION_COMUNAL', 'Acción comunal'),
    ('VICTIMAS', 'Víctimas'),
    ('JOVENES', 'Jóvenes'),
    ('MUJERES', 'Mujeres'),
    ('INFANCIA_ADOLESCENCIA', 'Infancia y adolescencia'),
    ('POBLACIONES_VULNERABLES', 'Poblaciones vulnerables'),
    ('PROPIEDAD_HORIZONTAL', 'Propiedad horizontal'),
    ('GRUPOS_ETNICOS', 'Grupos étnicos'),
    ('PLANEACION_PARTICIPATIVA', 'Planeación participativa'),
    ('PAZ', 'Paz'),
    ('PARTICIPACION_CIUDADANA', 'Participación ciudadana'),
    ('PARTICIPACION_POLITICA', 'Participación política'),
]


###  43.3

OPCIONES_OFERTA_SERVICIOS_ER = [
    ('DISCRIMINACION_RELIGIOSA', 'Discriminación religiosa'),
    ('DESCONOCIMIENTO_INSTANCIAS', 'Desconocimiento de las instancias existentes'),
    ('FALTA_FORMACION_TECNICA', 'Falta de formación técnica'),
    ('NO_INTERES_EN_PARTICIPAR', 'No tiene interés en participar'),
    ('SIN_DIFICULTADES', 'No ha tenido dificultades'),
]


###  43.4

OPCIONES_OFERTA_SERVICIOS_LIDERES = [
    ('LIDERAZGO', 'Formación en liderazgo'),
    ('GESTION_DE_PAZ', 'Formación en gestión de paz'),
    ('NORMATIVIDAD_RELIGIOSA', 'Formación en normatividad religiosa'),
    ('FORMULACION_DE_PROYECTOS_SOCIALES', 'Formulación y presentación de proyectos sociales'),
    ('TEMATICA_TRIBUTARIA', 'Formación en temática tributaria'),
    ('GERENCIA_Y_GESTION', 'Gerencia y Gestión'),
    ('FORTALECIMIENTO_ORGANIZACIONAL_ADMINISTRATIVO', 'Fortalecimiento organizacional y administrativo'),
    ('OTRA', 'Otra (s)'),
    ('NINGUNO', 'Ninguno'),
]



###  44


OPCIONES_PARTICIPACION_POBLACION_SOCIALES = [
    ('INVITACIONES_COMUNICACIONES', 'A través de invitaciones y comunicaciones regulares '
                                    'a los miembros de la comunidad.'),
    ('EVENTOS_ACTIVIDADES_ATRACTIVAS', 'Organizando eventos y actividades atractivas para la participación.'),
    ('TOMA_DECISIONES_PARTICIPATIVA', 'Fomentando la toma de decisiones '
                                      'participativa en la planificación de actividades.'),
    ('OPORTUNIDADES_VOLUNTARIADO', 'Ofreciendo oportunidades de voluntariado y servicio comunitario.'),
    ('FORMACION_GRUPOS_COMITES', 'Facilitando la formación de grupos y comités de interés.'),
    ('APOYO_RECURSOS_DESARROLLO_TALENTOS', 'Brindando apoyo y recursos para el '
                                           'desarrollo de talentos y habilidades de la comunidad.'),
    ('PLATAFORMAS_EN_LINEA_REDES_SOCIALES', 'Utilizando plataformas en línea o redes sociales '
                                            'para la comunicación y participación.'),
    ('NO_PROMUEVE_PARTICIPACION', 'No promovemos activamente la participación '
                                  'de la población local en nuestras actividades sociales.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]

###  45

OPCIONES_IMPACTO_CULTURAL = [
    ('IMPACTO_SIGNIFICATIVO', 'Sí, hemos tenido un impacto significativo en la promoción de valores, ética y cultura.'),
    ('IMPACTO_MODERADO', 'Sí, hemos tenido un impacto moderado en estos aspectos.'),
    ('NO_IMPACTO_SIGNIFICATIVO', 'No hemos tenido un impacto significativo en estos aspectos.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]

###  46

OPCIONES_BENEFICIARIOS_ACTIVIDADES = [
    ('MENOS_100_PERSONAS', 'Menos de 100 personas.'),
    ('ENTRE_100_Y_500_PERSONAS', 'Entre 100 y 500 personas.'),
    ('ENTRE_500_Y_1000_PERSONAS', 'Entre 500 y 1,000 personas.'),
    ('MAS_1000_PERSONAS', 'Más de 1,000 personas.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  47

OPCIONES_ACTIVIDADES_ODS = [
    ('PROYECTOS_EDUCACION', 'Proyectos de educación para promover la igualdad '
                            'de género y el acceso a la educación de calidad.'),
    ('INICIATIVAS_SALUD', 'Iniciativas de salud para mejorar el bienestar '
                          'y la atención médica de comunidades vulnerables.'),
    ('PROGRAMAS_ALIMENTACION_NUTRICION', 'Programas de alimentación y nutrición '
                                         'para combatir la malnutrición y el hambre.'),
    ('PROYECTOS_VIVIENDA', 'Proyectos de vivienda y desarrollo de infraestructura '
                           'para reducir la desigualdad en el acceso a la vivienda adecuada.'),
    ('PROGRAMAS_EMPRENDIMIENTO', 'Programas de empoderamiento económico para combatir '
                                 'la pobreza y promover el empleo digno.'),
    ('INICIATIVAS_MEDIO_AMBIENTE', 'Iniciativas de protección del medio ambiente y sostenibilidad.'),
    ('PROYECTOS_PROMOCION_PAZ', 'Proyectos de promoción de la paz, la justicia y las instituciones sólidas.'),
    ('OTRAS_ACTIVIDADES_ODS', 'Otras actividades relacionadas con los ODS.'),
    ('NO_ACTIVIDADES_ESPECIFICAS_ODS', 'No hemos llevado a cabo actividades '
                                       'específicas relacionadas con los ODS en Colombia.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  47.1

TEMAS_CHOICES = [
    ('PEDAGOGIA_PARA_LA_PAZ', 'Pedagogía para la paz, reconciliación.'),
    ('TALLERES_SENSIBILIZACION', 'Talleres de sensibilización para el perdón, paz y reconciliación.'),
    ('INCIDENCIA_PROMOCION_PAZ', 'Incidencia o participación en promoción en temas de paz.'),
    ('ACTIVIDADES_ARTISTICAS_LUDICAS_DEPORTIVAS', 'Actividades artísticas, lúdicas o deportivas '
                                                  'que aporten a la construcción de la paz.'),
    ('EDUCACION_PARA_EL_TRABAJO', 'Educación para el trabajo (capacitación laboral).'),
    ('EDUCACION_DERECHOS_HUMANOS', 'Educación en Derechos Humanos.'),
    ('PROYECTOS_PRODUCTIVOS', 'Proyectos productivos.'),
    ('PREVENCION_EMBARAZO_ADOLESCENTE', 'Programas de prevención de embarazo adolescente.'),
    ('PROMOCION_EQUIDAD_GENERO', 'Promoción de equidad de género.'),
    ('DERECHOS_SEXUALES_REPRODUCTIVOS', 'Derechos sexuales y reproductivos.'),
    ('SUPERACION_POBREZA', 'Superación de la pobreza.'),
    ('PROYECTOS_AMBIENTALES', 'Proyectos ambientales.'),
    ('LIDERAZGO_JUVENIL', 'Acción y liderazgo juvenil.'),
    ('LIDERAZGO_MUJERES', 'Acción y liderazgo de mujeres.'),
    ('PROYECTOS_INICIATIVA_JOVENES', 'Proyectos de iniciativa de jóvenes.'),
    ('PROYECTOS_INICIATIVA_MUJERES', 'Proyectos de iniciativa de mujeres.'),
    ('PREVENCION_ATENCION_VIOLENCIA_INTRA', 'Prevención y/o atención a la violencia intrafamiliar.'),
    ('PREVENCION_ATENCION_VIOLENCIA_CONTRA_MUJER', 'Prevención y/o atención a la violencia contra la mujer.'),
    ('PREVENCION_ATENCION_VIOLENCIA_SEXUAL', 'Prevención y/o atención a la violencia sexual.'),
    ('PREVENCION_ATENCION_VIOLENCIA_ESCOLAR', 'Prevención y/o atención a la violencia escolar.'),
    ('PREVENCION_TRABAJO_PANDILLAS_MICRO_TRAFICO', 'Prevención o trabajo en temas de pandillas y micro tráfico.'),
    ('TRABAJO_PROTECCION_GARANTIA_DERECHOS_DIVERSIDAD_ETNICA_CULTURAL', 'Trabajo en protección/garantía de '
                                                                        'derechos de la diversidad étnica y cultural.'),
    ('OBJECION_CONCIENCIA', 'Objeción de conciencia.'),
    ('PREVENCION_TRABAJO_VIOLENCIA_COTIDIANA_RIÑAS_CALLEJERAS', 'Prevención o trabajo en temas de '
                                                                'violencia cotidiana/riñas callejeras.'),
]
###  48

OPCIONES_ENFOQUE_ENTIDAD = [
    ('ENFOQUE_CONFESIONAL', 'Enfoque Confesional'),
    ('ENFOQUE_ASOCIATIVO', 'Enfoque Asociativo (Asociación, Federación, Confederación)'),
    ('ORGANIZACION_SECTOR_RELIGIOSO', 'Organización del Sector Religioso (OSR)'),
    ('BIIR', 'BIIR (Bienes de Interés de Interés Religioso)'),
    ('CONSEJO_CONSULTIVO_MUJERES', 'Consejo Consultivo de Mujeres'),
    ('CONSEJO_JUVENTUD', 'Consejo de Juventud'),
    ('GESTORES_PAZ_RECONCILIACION', 'Gestores de Paz y Reconciliación'),
    ('ENFOQUE_RURAL', 'Enfoque Rural'),
    ('DEPARTAMENTO_DISTRITO_MUNICIPAL', 'Departamento, Distrito y Municipal'),
    ('MEDIOS_COMUNICACION', 'Medios de Comunicación (Emisoras, Canales, Periódicos)'),
    ('EDUCACION', 'Educación'),
    ('PAZ', 'Paz'),
    ('OTRO', 'Otro (por favor, especifique)'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  49


OPCIONES_SI_NO_LIDER = [
    ('SI', 'Sí'),
    ('NO', 'No'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable'),
]
###  50

OPCIONES_SEGURO_MEDICO = [
    ('SEGURO_COMPLETO', 'Sí, proporciona un seguro médico completo.'),
    ('SEGURO_BASICO', 'Sí, proporciona un seguro médico básico.'),
    ('NO_PROPORCIONA', 'No, no proporciona seguro médico.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  51

PLAN_JUBILACION_CHOICES = [
    ('OFRECE_PLAN', 'Sí, ofrece un plan de jubilación o pensiones.'),
    ('NO_OFRECE_PLAN', 'No, no ofrece ningún plan de jubilación o pensiones.'),
    ('NO_SEGURO_PLAN_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  52

APOYO_ECONOMICO_CHOICES = [
    ('BRINDA_APOYO', 'Sí, brinda apoyo económico en casos de enfermedad o emergencia.'),
    ('NO_BRINDA_APOYO', 'No, no brinda apoyo económico en estos casos.'),
    ('NO_SEGURO_APOYO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  53


SEGURO_VIDA_INCAPACIDAD_CHOICES = [
    ('OFRECE_SEGURO', 'Sí, ofrece seguro de vida y/o seguro de incapacidad.'),
    ('NO_OFRECE_SEGURO', 'No, no ofrece este tipo de seguro.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  54


FORMACION_SEGURIDAD_SOCIAL_CHOICES = [
    ('SE_PROPORCIONA', 'Sí, se proporciona formación y capacitación sobre seguridad social y beneficios.'),
    ('NO_SE_PROPORCIONA', 'No, no se proporciona formación ni capacitación en este tema.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  55

DESAFIOS_SEGURIDAD_SOCIAL_CHOICES = [
    ('ENFRENTADO_DESAFIOS', 'Sí, he enfrentado desafíos relacionados con la seguridad social.'),
    ('SIN_DESAFIOS', 'No, no he enfrentado desafíos en este aspecto.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.'),
]
###  56

BENEFICIOS_ADICIONALES_CHOICES = [
    ('MAS_COBERTURA_MEDICA', 'Más cobertura médica.'),
    ('MEJORES_PLANES_JUBILACION', 'Mejores planes de jubilación.'),
    ('MAYOR_APOYO_FINANCIERO', 'Mayor apoyo financiero en casos de emergencia.'),
    ('OTROS', 'Otros (por favor, especifique).'),
    ('NO_SUGERENCIAS_ADICIONALES', 'No tengo sugerencias adicionales.'),
    ('NO_SEGURO_NO_APLICABLE', 'No estoy seguro/No aplicable.')
]
###  57

PARTICIPACION_HUMANITARIA_CHOICES = [
    ('SI', 'Sí'),
    ('NO', 'No'),
    ('NO_SABE_NO_APLICA', 'No sabe/No aplica'),
]
###  58

ACTIVIDADES_HUMANITARIAS_CHOICES = [
    ('SI_COLABORA_REGULARMENTE', 'Sí, colabora regularmente con agencias gubernamentales '
                                 'en proyectos humanitarios en Colombia'),
    ('SI_COLABORA_OCASIONALMENTE', 'Sí, colabora ocasionalmente con agencias gubernamentales '
                                   'en proyectos humanitarios en Colombia.'),
    ('SI_COLABORA_CON_ORGANIZACIONES_NO_RELIGIOSAS', 'Sí, colabora con organizaciones '
                                                     'no religiosas en proyectos humanitarios en Colombia.'),
    ('NO_NO_COLABORA', 'No, nuestra organización religiosa no colabora con agencias '
                       'gubernamentales ni organizaciones no religiosas en proyectos humanitarios en Colombia.'),
    ('NO_APLICA', 'No aplicable / No estamos involucrados en proyectos humanitarios en Colombia.'),
]
###  59

ALCANCE_GEOGRAFICO_CHOICES_HUMANITARIAS = [
    ('NIVEL_NACIONAL', 'Nivel nacional: Nuestras actividades humanitarias abarcan todo el territorio de Colombia.'),
    ('REGIONAL', 'Regional: Nuestras actividades se centran en una región específica o algunas regiones de Colombia.'),
    ('LOCAL', 'Local: Nos enfocamos en comunidades o áreas específicas dentro de una región.'),
    ('INTERNACIONAL', 'Internacional: Nuestra organización también realiza actividades humanitarias fuera de Colombia.'),
    ('NO_APLICA_ALCANCE_GEOGRAFICO', 'No aplicable: No estamos involucrados en actividades humanitarias en Colombia.'),
]
###  60

INTERACCION_COMUNIDAD_CHOICES = [
    ('PROGRAMAS_PARTICIPACION_COMUNITARIA', 'Establecemos programas de participación comunitaria y '
                                            'colaboramos activamente con líderes locales.'),
    ('EVENTOS_TALLERES_ABIERTOS', 'Organizamos eventos y talleres abiertos a la comunidad para '
                                  'fomentar la participación y la colaboración.'),
    ('COORDINACION_ORGANIZACIONES_COMUNITARIAS', 'Trabajamos en estrecha coordinación con '
                                                 'organizaciones comunitarias existentes en Colombia.'),
    ('PROMOCION_VOLUNTARIADO_LOCAL', 'Promovemos la participación de voluntarios locales '
                                     'en nuestros proyectos humanitarios.'),
    ('CONCIENCIACION_EDUCACION_COMUNITARIA', 'Realizamos campañas de concienciación y '
                                             'educación en la comunidad sobre temas humanitarios.'),
    ('TODAS_LAS_ANTERIORES', 'Todas las anteriores.'),
    ('NO_INTERACTUA_DIRECTAMENTE', 'No interactuamos de manera directa con la comunidad '
                                   'local en Colombia en relación con el actuar humanitario.'),
]
###  61

ENFOQUE_SERVICIOS_HUMANITARIOS_CHOICES = [
    ('grupo_vulnerables', 'Sí, nos enfocamos en brindar servicios humanitarios a grupos '
                          'vulnerables como niños, ancianos o personas con discapacidades.'),
    ('comunidades_indigenas', 'Sí, nuestras actividades humanitarias están dirigidas '
                              'principalmente a comunidades indígenas o afrocolombianas.'),
    ('desastres_naturales', 'Sí, nos centramos en brindar servicios a personas '
                            'afectadas por desastres naturales en Colombia.'),
    ('desplazados_conflictos', 'Sí, colaboramos con organizaciones que trabajan específicamente con '
                               'grupos desplazados por conflictos en Colombia.'),
    ('general_sociedad_colombiana', 'No, ofrecemos servicios humanitarios de manera general a '
                                    'la sociedad colombiana sin focalizarnos en grupos específicos.'),
]
###  62

PARTICIPACION_COMUNITARIA_CHOICES = [
    ('CAPACITACION_LIDERES_COMUNITARIOS', 'Fomentamos la capacitación y formación de líderes '
                                          'comunitarios locales para que participen en la planificación y '
                                          'ejecución de proyectos humanitarios.'),
    ('REUNIONES_ASAMBLEAS_ABIERTAS', 'Organizamos reuniones y asambleas abiertas a la '
                                     'comunidad para recoger sus opiniones y sugerencias sobre '
                                     'nuestras actividades humanitarias.'),
    ('GRUPOS_VOLUNTARIOS_LOCALES', 'Establecemos grupos de voluntarios locales que colaboran activamente '
                                   'en la implementación de proyectos.'),
    ('COLABORACION_ORGANIZACIONES_COMUNITARIAS', 'Colaboramos estrechamente con organizaciones comunitarias '
                                                 'existentes en Colombia para trabajar de manera conjunta en '
                                                 'proyectos humanitarios.'),
    ('PARTICIPACION_COMUNIDAD_TOMA_DECISIONES', 'Promovemos la participación de la comunidad '
                                                'en la toma de decisiones relacionadas con nuestros '
                                                'proyectos humanitarios a través de consultas y encuestas.'),
    ('TODAS_LAS_ANTERIORES_PARTICIPACION_COMUNITARIA', 'Todas las anteriores.'),
    ('NO_PROMOVEMOS_PARTICIPACION_COMUNITARIA', 'No promovemos la participación de la '
                                                'población local en nuestras actividades humanitarias.'),
]
###  63

DESAFIOS_CHOICES = [
    ('LIMITACIONES_FINANCIERAS', 'Limitaciones financieras y dificultades para recaudar fondos suficientes.'),
    ('ACCESO_LIMITADO_AREAS_REMOTAS', 'Acceso limitado a áreas remotas o afectadas por conflictos.'),
    ('CAMBIOS_LEGISLACION_POLITICAS', 'Cambios en la legislación o políticas '
                                      'gubernamentales que afectan nuestras actividades.'),
    ('FALTA_PERSONAL_VOLUNTARIOS_CAPACITADOS', 'Falta de personal y voluntarios capacitados.'),
    ('COMPETENCIA_CON_OTRAS_ORGANIZACIONES', 'Competencia con otras organizaciones por recursos y apoyo.'),
    ('OBSTACULOS_CULTURALES_RELIGIOSOS', 'Obstáculos culturales o religiosos en la relación con la comunidad local.'),
    ('DESCONFIANZA_POBLACION_LOCAL', 'Desconfianza de la población local hacia organizaciones religiosas.'),
    ('PROBLEMAS_SEGURIDAD_PERSONAL_VOLUNTARIOS', 'Problemas de seguridad para nuestro personal y voluntarios.'),
    ('CAMBIOS_NECE_SOCIEDAD_SERVICIO', 'Cambios en las necesidades de la población a la que servimos.'),
    ('OTROS_DESAFIOS', 'Otros desafíos no mencionados anteriormente.'),
]
###  64

PLANES_PERSPECTIVAS_CHOICES = [
    ('AMPLIAR_OPERACIONES', 'Ampliar nuestras operaciones humanitarias en nuevas áreas geográficas en Colombia.'),
    ('DIVERSIFICAR_MEJORAR_PROGRAMAS', 'Diversificar y mejorar nuestros programas y servicios humanitarios.'),
    ('FORTALECER_COLABORACION', 'Fortalecer la colaboración con otras organizaciones humanitarias en Colombia.'),
    ('INCREMENTAR_RECAUDACION_FONDOS', 'Incrementar nuestros esfuerzos de recaudación '
                                       'de fondos para financiar proyectos a largo plazo.'),
    ('MEJORAR_PARTICIPACION_EMPODERAMIENTO', 'Mejorar la participación y el '
                                             'empoderamiento de la comunidad local en la toma de decisiones.'),
    ('INVERTIR_FORMACION_CAPACITACION', 'Invertir en la formación y capacitación '
                                        'continua de nuestro personal y voluntarios.'),
    ('ADAPTARNOS_CAMBIANTES_NECESIDADES', 'Adaptarnos a las cambiantes necesidades de la población colombiana a la que servimos.'),
    ('EVALUAR_MEDIR_IMPACTO', 'Evaluar y medir regularmente el impacto de nuestros proyectos humanitarios.'),
    ('BUSCAR_OPORTUNIDADES_PROMOVER_PAZ', 'Buscar oportunidades para promover '
                                          'la paz y la reconciliación en áreas afectadas por conflictos.'),
    ('TODAS_LAS_ANTERIORES', 'Todas las anteriores.'),
    ('NO_TENEMOS_PLANES', 'No tenemos planes futuros específicos en este momento.'),
]
###  65

ACTIVIDADES_CUIDADO_CHOICES = [
    ('MANTENIMIENTO_VESTUARIO', 'Mantenimiento del vestuario (Lavar, planchar o guardar '
                                'la ropa de las personas del hogar, Reparar ropa, cobijas, '
                                'maletas o calzado de las personas del hogar, Llevar o recoger '
                                'ropa o zapatos de la lavandería o zapatería)'),
    ('LIMPIEZA_MANTENIMIENTO_REPARACION', 'Limpieza, mantenimiento y reparación (Barrer, trapear, tender camas, '
                                          'sacudir el polvo, sacar la basura; Cuidar mascotas o animales de compañía, '
                                          'cuidar el jardín, limpiar el vehículo; Traer combustible para uso '
                                          'de la comunidad diferente a leña; Reparar o hacer instalaciones en '
                                          'otras viviendas diferente a la suya)'),
    ('CUIDADO_FISICO', 'Cuidado físico como apoyo a integrantes de la comunidad u otras comunidades '
                       '(Alimentar a una persona o ayudarle a hacerlo; Bañar o vestir a una persona o '
                       'ayudarle a hacerlo; Suministrar medicamentos, hacer terapias o dar tratamiento a enfermedades)'),
    ('CUIDADO_NINOS', 'Cuidado de niños, niñas y adolescentes integrantes de su comunidad u otras comunidades '
                      '(Jugar; Leer o contar cuentos; Llevar al parque)'),
    ('APOYO_PERSONAS', 'Apoyo a personas de su comunidad u otras comunidades (Ayudar con tareas o trabajos escolares; '
                       'Acompañar a citas médicas, odontológicas, urgencias, terapias u otras atenciones en salud. '
                       'Llevar o traer a personas del hogar al sitio de estudio, '
                       'trabajo o a eventos culturales deportivos o recreativos)'),
    ('CULTIVO_COSECHA', 'Cultivo y cosecha de productos agrícolas o de huerta/cuidado de '
                        'animales para el consumo de su comunidad)'),
    ('OTRAS_ACTIVIDADES', 'Otras'),
]