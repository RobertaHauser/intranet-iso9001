from django.db import models

# Create your models here.
class for_reh_001(models.Model):
    escolaridade_choices=(("Alfabetizado","Alfabetizado"),("Fundamental incompleto","Fundamental incompleto"),("Fundamental completo","Fundamental completo"),\
                         ("Médio incompleto","Médio incompleto"),("Médio completo","Médio completo"),\
                         ("Superior incompleto","Superior incompleto"),("Superior completo","Superior completo"))
    treinamento_choices=(("sim","sim"),("não","não"))
    experiencia_choices=(("sim","sim"),("não","não"))

    funcao=models.CharField(verbose_name="Função",max_length=194,unique=True)
    escolaridade=models.CharField(verbose_name="Escolaridade",max_length=194,choices=escolaridade_choices,blank=False,null=False)
    treinamentoopc=models.CharField(verbose_name="Necessário treinamento",max_length=5,choices=treinamento_choices,blank=False,null=False)
    treinamento=models.CharField(verbose_name="Treinamento requerido",max_length=194,blank=True,null=True)
    experienciaopc=models.CharField(verbose_name="Necessário experiencia",max_length=5,choices=experiencia_choices,blank=False,null=False)
    experiencia=models.CharField(verbose_name="Experiência requerida",max_length=194,blank=True,null=True)

    class Meta:
        verbose_name="FOR-REH-001"
        verbose_name_plural="FOR-REH-001"
        db_table="for_reh_001"

    def __str__(self):
        return self.funcao