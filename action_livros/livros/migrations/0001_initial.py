# Generated by Django 2.2.5 on 2019-09-05 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_livro', models.CharField(max_length=300)),
                ('isbn', models.CharField(max_length=13)),
                ('data_criacao', models.DateField()),
                ('num_paginas', models.IntegerField()),
            ],
            options={
                'db_table': 'livros',
            },
        ),
    ]
