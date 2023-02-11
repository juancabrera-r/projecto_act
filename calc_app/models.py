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

    # @classmethod
    # def crear_ciclo(cls, descripcionCiclo):
    #     ciclo = cls(descripcionCiclo=descripcionCiclo)
    #     return ciclo

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


    def __str__(self):
        return '%s %s %s' % (self.ciclo, self.id_modulo, self.siglasModulo)

#Modelo del  Actividades
class Actividades(models.Model):
    """
    Tabla que registra los distintos módulos
    siglasModulo -> abreviatura/siglas del módulo
    id_modulo -> identificación del módulo, se genera automático, único
    descripcionModulo -> Nombre del módulo de ciclo, único
    """
    id_act = models.AutoField(primary_key=True, unique=True)
    numAct = models.IntegerField()
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    n_RA_1 = models.IntegerField(default=0)
    n_CE_1 = models.IntegerField(default=0)
    n_RA_2 = models.IntegerField(default=0)
    n_CE_2 = models.IntegerField(default=0)
    n_RA_3 = models.IntegerField(default=0)
    n_CE_3 = models.IntegerField(default=0)
    n_RA_4 = models.IntegerField(default=0)
    n_CE_4 = models.IntegerField(default=0)
    n_RA_5 = models.IntegerField(default=0)
    n_CE_5 = models.IntegerField(default=0)
    n_RA_6 = models.IntegerField(default=0)
    n_CE_6 = models.IntegerField(default=0)
    n_RA_7 = models.IntegerField(default=0)
    n_CE_7 = models.IntegerField(default=0)
    n_RA_8 = models.IntegerField(default=0)
    n_CE_8 = models.IntegerField(default=0)
    n_RA_9 = models.IntegerField(default=0)
    n_CE_9 = models.IntegerField(default=0)
    n_RA_10 = models.IntegerField(default=0)
    n_CE_10 = models.IntegerField(default=0)

    def __str__(self):
        return str(self.modulo)

