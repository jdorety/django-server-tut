# Generated by Django 3.0.4 on 2020-04-01 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200401_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='language',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
