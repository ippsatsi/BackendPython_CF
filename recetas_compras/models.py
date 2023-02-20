from django.db import models
from django.utils import timezone
from django.urls import reverse


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
        ('FRU', 'Frutas'),
        ('GRA','Granos,Cereales'),
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
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse("detalle_ingrediente", args=[str(self.id)])


class Receta(models.Model):
    TYPE_INGREDIENTE_PRINCIPAL = [
        ("AVE", "Aves"),
        ("RES", "Res"),
        ("CER", "Cerdo"),
        ("MAR", "Marino"),
        ("OVO", "Huevos"),
        ('CON', 'Conservas'),
        ("OTR", "Otros"),
    ]
    nombre = models.CharField(max_length=100)
    ingr_principal = models.CharField(
        max_length= 3,
        choices= TYPE_INGREDIENTE_PRINCIPAL,
    )
    ingredientes = models.ManyToManyField(Ingrediente, related_name= 'get_ingredientes',  through='M2MRecetario')
    image = models.ImageField(upload_to="recetas_compras/photos")
    preparacion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        pass
    
    def get_absolute_url(self):
        return reverse("detalle_receta", args=[str(self.id)])

class M2MRecetario(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete= models.PROTECT)
    receta = models.ForeignKey(Receta, on_delete= models.CASCADE)
    cantidad = models.DecimalField(max_digits=3, decimal_places=1, )

    def __str__(self):
        return f'{self.receta} - {self.ingrediente}'

    class Meta:
        pass


class Semana(models.Model):
    nombre = models.CharField(max_length=100)
    recetas = models.ManyToManyField(Receta, related_name= 'get_recetas')
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse("detalle_semana", args=[str(self.id)])