# Generated by Django 5.0.2 on 2024-03-14 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes_Mascotas', '0003_alter_mascota_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_mascotas'),
        ),
    ]