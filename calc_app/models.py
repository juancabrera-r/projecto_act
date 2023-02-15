from django.db import models

# Create your models here.

#Modelo del Ciclo
class Ciclo(models.Model):
    """
    Tabla que registra los distintos cursos
        id_curso -> identificación del curso, se genera automático
        descripcionCurso -> Nombre del curso (ciclo), único
    """
    id_ciclo = models.AutoField(primary_key=True, unique=True)
    descripcionCiclo = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return '%s' % (self.descripcionCiclo)

#Modelo del  Módulo
class Modulo(models.Model):
    """
    Tabla que registra los distintos módulos
        ciclo = hereda de Ciclo
        siglasModulo -> abreviatura/siglas del módulo
        id_modulo -> identificación del módulo, se genera automático, único
        descripcionModulo -> Nombre del módulo de ciclo, único
    """
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    id_modulo = models.AutoField(primary_key=True, unique=True)
    siglasModulo = models.CharField(max_length=10,unique=True)
    descripcionModulo = models.CharField(max_length=264, unique=True)
    numRA = models.IntegerField()
    arrayRACE = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '%s' % (self.descripcionModulo)

#Modelo del  Actividades
class Actividades(models.Model):
    """
    Tabla que registra las distintas actividades
        id_actv -> identificación de la actividad, se genera automático, único
        numAct -> número de actividades que se desea realizar
        ciclo -> hereda de Ciclo
        modulo -> hereda de Modulo
    """
    id_act = models.AutoField(primary_key=True, unique=True)
    numAct = models.IntegerField()
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.modulo)

