# Generated by Django 4.1.3 on 2023-01-22 19:51

import app.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('A', 'Aula'), ('S', 'Salon'), ('L', 'Laboratorio'), ('D', 'Departamento')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('local', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.local')),
                ('fecha', models.DateField(auto_now=True)),
                ('faltante', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'La cantidad debe ser mayor o igual a 0')])),
                ('sobrante', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'La cantidad debe ser mayor o igual a 0')])),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('A', 'Aprobado'), ('D', 'Denegado')], default='P', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MedioBasico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mb', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^(MB|MB-)\\d{8,}$', 'Identificador Inválido')])),
                ('tipo', models.CharField(max_length=15, verbose_name='tipo')),
                ('estado', models.CharField(choices=[('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')], max_length=255, verbose_name='estado')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.local')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator('^[A-Za-z\\d]*$', 'Solo Letras y numeros , sin espacios')])),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[A-Za-záãäéëêíîóöúüñç\\s]*$', 'Solo Letras')])),
                ('apellidos', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[A-Za-záãäéëêíîóöúüñç\\s]*$', 'Solo Letras')])),
                ('ci', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])\\d{5}$', 'Carnet invalido')])),
                ('tfno', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^\\+53\\d{8}$', 'Teléfono invalido')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', app.models.OwnUserManager()),
            ],
        ),
    ]
