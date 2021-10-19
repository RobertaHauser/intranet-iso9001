from django.db import models

# Create your models here.
class tab_sgq_001(models.Model):
    requisito_num_original = models.CharField(verbose_name="N.Requisito(original)", max_length=184, unique=True, )
    requisito_txt_original = models.TextField(verbose_name="Descrição do requisito (original)", )
    requirement_num_original = models.CharField(verbose_name="N.Requirement (original)", max_length=184,)
    requirement_txt_original = models.TextField(verbose_name="Requirement description (original)", )


    class Meta:
        verbose_name = "TAB-SGQ-001"
        verbose_name_plural = "TAB-SGQ-001"
        db_table = "tab_sqg_001"

    def __str__(self):
        return self.requisito_num_original