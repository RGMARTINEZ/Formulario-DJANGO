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


class Encuesta(models.Model):
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

    #####
    poblacion_entidad = MultiSelectField(
        'De acuerdo con su cultura, pueblo o rasgos físicos, ¿Qué población atienden y ayuda su entidad religiosa? '
        '(puede marcar varias)', blank=False, null=False, max_length=255, default="", choices=TIPO_POBLACION)
    otra_poblacion_entidad = models.CharField(
        'Otro tipo de población seleccionado', blank=True, null=True, max_length=255)

    ####
    grupos_personas = MultiSelectField(
        'Dentro del siguiente grupo de personas, ¿Cuál atiende y beneficia su entidad religiosa? '
        '(puede marcar varias)', blank=False, null=False, max_length=255, default="", choices=GRUPOS_PERSONAS)
    otros_grupos_personas = models.CharField(
        'Otro grupo de personas seleccionado', blank=True, null=True, max_length=255)

    ####
    atiende_poblacion_discapacitada = models.CharField(
        '¿Atiende población en la entidad religiosa en condición de discapacidad?',
        blank=False, null=False, max_length=255, default=OPCIONES_SI_NO[0][0], choices=OPCIONES_SI_NO)

    tipos_discapacidades = MultiSelectField(
        'Si respondió si en la pregunta anterior ¿Qué tipo de discapacidad '
        'tiene la población que atiende su entidad religiosa?',
        blank=True, null=True, max_length=255, default="", choices=OPCIONES_CONDICION_DISCAPACIDAD)

    otra_discapacidad = models.CharField(
        'Otro discapacidad seleccionada', blank=True, null=True, max_length=255)

    #####
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







