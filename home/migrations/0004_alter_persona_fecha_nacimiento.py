# Generated by Django 4.1.1 on 2022-09-30 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_persona_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
