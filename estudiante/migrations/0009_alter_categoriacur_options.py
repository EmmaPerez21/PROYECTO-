# Generated by Django 4.2.5 on 2023-10-06 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0008_rename_categoriacurso_categoriacur_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriacur',
            options={'verbose_name': 'categoriaCur', 'verbose_name_plural': 'categoriasCur'},
        ),
    ]
