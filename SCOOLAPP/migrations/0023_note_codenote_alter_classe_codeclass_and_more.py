# Generated by Django 4.1.4 on 2023-01-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCOOLAPP', '0022_remove_note_codenote'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='codeNote',
            field=models.CharField(default='NOTE-', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='classe',
            name='codeClass',
            field=models.CharField(default='CLASS-', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='MatriculeElev',
            field=models.CharField(default='ELEV-', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='MatriculeProf',
            field=models.CharField(default='PROF-', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='CodeTyp',
            field=models.CharField(default='TYP-', max_length=100, unique=True),
        ),
    ]
