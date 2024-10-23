# Generated by Django 5.1.2 on 2024-10-22 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testeDjango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='anotacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anotacao', models.TextField()),
                ('data_adicao', models.DateTimeField(auto_now_add=True)),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testeDjango.topic')),
            ],
        ),
    ]