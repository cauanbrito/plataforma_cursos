# Generated by Django 5.0.6 on 2024-05-15 01:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_comentarios'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotasAulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(choices=[('p', 'Péssimo'), ('r', 'Ruim'), ('re', 'Regular'), ('b', 'bom'), ('o', 'Ótimo')], max_length=50)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.aulas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
