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

    @classmethod
    def crear_ciclo(cls, descripcionCiclo):
        ciclo = cls(descripcionCiclo=descripcionCiclo)
        return ciclo

    def __str__(self):
        return '%s %s' % (self.id_ciclo, self.descripcionCiclo)

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
    id_modulo = models.AutoField(primary_key=True)
    siglasModulo = models.CharField(max_length=10,unique=True)
    descripcionModulo = models.CharField(max_length=264, unique=True)
    numRA = models.IntegerField()
    numCE = models.IntegerField()

    def __str__(self):
        return '%s, %s' % (self.siglasModulo, self.descripcionModulo)

#Modelo del  Actividades
class Actividades(models.Model):
    """
    Tabla que registra los distintos módulos
    siglasModulo -> abreviatura/siglas del módulo
    id_modulo -> identificación del módulo, se genera automático, único
    descripcionModulo -> Nombre del módulo de ciclo, único
    """
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    numAct = models.IntegerField()
    numRA = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    numCE = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    pesoCE1 = models.IntegerField()
    pesoCE2 = models.IntegerField()
    pesoCE3 = models.IntegerField()
    pesoCE4 = models.IntegerField()
    pesoCE5 = models.IntegerField()
    pesoCE6 = models.IntegerField()
    pesoCE7 = models.IntegerField()
    pesoCE8 = models.IntegerField()
    pesoCE9 = models.IntegerField()
    pesoCE10 = models.IntegerField()

    def __str__(self):
        return self.numAct