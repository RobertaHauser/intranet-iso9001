# Generated by Django 3.2.8 on 2021-10-14 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaopessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='for_reh_001',
            name='experienciaopc',
            field=models.CharField(choices=[('sim', 'sim'), ('não', 'não')], default='', max_length=5, verbose_name='Necessário experiencia'),
            preserve_default=False,
        ),
    ]
