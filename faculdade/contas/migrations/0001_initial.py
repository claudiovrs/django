# Generated by Django 2.0.3 on 2018-05-18 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('ra', models.CharField(max_length=10, verbose_name='RA')),
                ('senha', models.CharField(max_length=50, verbose_name='Senha')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
            ],
        ),
    ]
