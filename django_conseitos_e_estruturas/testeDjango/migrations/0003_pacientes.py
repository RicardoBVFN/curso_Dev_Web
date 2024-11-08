# Generated by Django 5.1.2 on 2024-10-31 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testeDjango', '0002_anotacoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='pacientes',
            fields=[
                ('chave', models.AutoField(primary_key=True, serialize=False)),
                ('nome_completo', models.TextField(max_length=150)),
                ('idade', models.IntegerField()),
                ('sexo', models.TextField(max_length=9)),
                ('curiosidade', models.TextField(max_length=200)),
                ('data_adicao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
