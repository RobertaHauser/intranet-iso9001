from django.db import models

# Create your models here.
class for_reh_001(models.Model):
    experiencia_choices=(("sim","sim"),("não","não"))


    funcao=models.CharField(verbose_name="Função",max_length=194,unique=True)
    treinamento=models.CharField(verbose_name="Treinamento requerido",max_length=194,blank=True,null=True)
    experiencia=models.CharField(verbose_name="Experiência requerida",max_length=194,blank=True,null=True)
    experienciaopc=models.CharField(verbose_name="Necessário experiencia",max_length=5,choices=experiencia_choices,blank=False,null=False)

    class Meta:
        verbose_name="FOR-REH-001"
        verbose_name_plural="FOR-REH-001"
        db_table="for_reh_001"

    def __str__(self):
        return self.funcao