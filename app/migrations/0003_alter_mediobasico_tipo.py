# Generated by Django 4.1.3 on 2023-01-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_mediobasico_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediobasico',
            name='tipo',
            field=models.CharField(max_length=15),
        ),
    ]
