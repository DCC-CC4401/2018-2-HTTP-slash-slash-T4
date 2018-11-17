# Generated by Django 2.1.3 on 2018-11-17 19:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Coevaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(choices=[('abierta', 'Abierta'), ('cerrada', 'Cerrada'), ('publicada', 'Publicada')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('seccion', models.IntegerField(default=1)),
                ('anho', models.IntegerField()),
                ('semestre', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('historial', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info_Coevaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondida', models.BooleanField()),
                ('nota', models.FloatField(blank=True, max_length=3, null=True)),
                ('coevaluacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Coevaluacion')),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Integrante_Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=30)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Integrante_Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Curso')),
                ('equipo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(help_text='Ingrese rut sin puntos ni guión', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='integrante_equipo',
            name='rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Usuario'),
        ),
        migrations.AddField(
            model_name='integrante_curso',
            name='rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Usuario'),
        ),
        migrations.AddField(
            model_name='info_coevaluacion',
            name='rut_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Usuario'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='curso_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Usuario'),
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together={('nombre', 'seccion', 'anho', 'semestre')},
        ),
        migrations.AddField(
            model_name='coevaluacion',
            name='curso_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Curso'),
        ),
        migrations.AddField(
            model_name='admin',
            name='usuario_rut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coev.Usuario'),
        ),
        migrations.AlterUniqueTogether(
            name='integrante_equipo',
            unique_together={('equipo_id', 'curso_id', 'rut')},
        ),
        migrations.AlterUniqueTogether(
            name='integrante_curso',
            unique_together={('rut', 'curso')},
        ),
        migrations.AlterUniqueTogether(
            name='info_coevaluacion',
            unique_together={('curso_id', 'coevaluacion_id', 'rut_usuario')},
        ),
        migrations.AlterUniqueTogether(
            name='equipo',
            unique_together={('curso_id', 'nombre')},
        ),
    ]