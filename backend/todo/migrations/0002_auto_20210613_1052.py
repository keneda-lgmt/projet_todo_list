# Generated by Django 3.1.4 on 2021-06-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='nom_categorie',
            field=models.CharField(max_length=100),
        ),
    ]
