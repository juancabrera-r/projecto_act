from django.db import models

# Create your models here.

#Modelo del Ciclo
class Ciclo(models.Model):
    """
    Tabla que registra los distintos cursos
    id_curso -> identificación del curso, se genera automático
    descripcionCurso -> Nombre del curso (ciclo), único
    """
    id_ciclo = models.AutoField(primary_key=True)
    descripcionCiclo = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.descripcionCiclo

#Modelo del  Módulo
class Modulo(models.Model):
    """
    Tabla que registra los distintos módulos
    siglasModulo -> abreviatura/siglas del módulo
    id_modulo -> identificación del módulo, se genera automático, único
    descripcionModulo -> Nombre del módulo de ciclo, único
    """
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    id_modulo = models.AutoField(primary_key=True)
    siglasModulo = models.CharField(max_length=10,unique=True)
    descripcionModulo = models.CharField(max_length=264, unique=True)
    numRA = models.IntegerField()
    numCE = models.IntegerField()

    def __str__(self):
        return self.siglasModulo, self.descripcionModulo

#Modelo del  Actividades
# class Actividades(models.Model):
#     """
#     Tabla que registra los distintos módulos
#     siglasModulo -> abreviatura/siglas del módulo
#     id_modulo -> identificación del módulo, se genera automático, único
#     descripcionModulo -> Nombre del módulo de ciclo, único
#     """
#     ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
#     id_actividad = models.IntegerField()
#     id_modulo = models.AutoField(primary_key=True)
#     siglasModulo = models.CharField(max_length=10,unique=True)
#     descripcionModulo = models.CharField(max_length=264, unique=True)
#     numRA = models.IntegerField()
#     numCE = models.IntegerField()
#
#     def __str__(self):
#         return self.siglasModulo, self.descripcionModulo