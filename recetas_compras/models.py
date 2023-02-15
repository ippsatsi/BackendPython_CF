from django.db import models
from django.utils import timezone


class Ingrediente(models.Model):
    TYPE_UNIDAD = [
        ("PEN", "Soles"),
        ("KG", "Kilos"),
        ("LT", "Litros"),
        ("GR", "Gramos"),
        ("DOC", "Docena(s)"),
        ("UN", "Unidad(es)"),
    ]

    TYPE_INGREDIENTE = [
        ("CRN", "Carnes"),
        ("VRD", "Verduras"),
        ("ESP", "Especias"),
        ("LAC", "Lacteos"),
        ("OVO", "Huevos"),
        ('FRU', 'Frutas')
        ("OTR", "Otros"),
    ]
    nombre = models.CharField(max_length=100)
    tipo_ingrediente = models.CharField(
        max_length= 3,
        choices= TYPE_INGREDIENTE,
        default= 'OTR'
    )
    tipo_unidad = models.CharField(
        max_length= 3,
        choices= TYPE_UNIDAD,
        default='UN'
    )
    created_at = models.DateTimeField(default=timezone.now)


class Receta(models.Model):
    TYPE_INGREDIENTE_PRINCIPAL = [
        ("AVE", "Aves"),
        ("RES", "Res"),
        ("CER", "Cerdo"),
        ("MAR", "Marino"),
        ("OVO", "Huevos"),
        ('CON', 'Conservas')
        ("OTR", "Otros"),
    ]
    nombre = models.CharField(max_length=100)
    ingr_principal = models.CharField(
        max_length= 3,
        choices= TYPE_INGREDIENTE_PRINCIPAL,
    )
    ingredientes = models.ManyToManyField(Ingrediente, related_name= 'get_ingredientes',  through='M2M_Recetarios')
    image = models.ImageField(upload_to="recetas_compras/photos")
    preparacion = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class M2M_Recetarios(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete= models.PROTECT)
    receta = models.ForeignKey(Receta, on_delete= models.CASCADE)
    cantidad = models.DecimalField(max_digits=3, decimal_places=1, )

class Semana(models.Model):
    pass

