# Generated by Django 2.2.5 on 2019-09-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_editora', models.CharField(max_length=300)),
                ('data_fundacao', models.DateField()),
            ],
            options={
                'db_table': 'editoras',
            },
        ),
    ]