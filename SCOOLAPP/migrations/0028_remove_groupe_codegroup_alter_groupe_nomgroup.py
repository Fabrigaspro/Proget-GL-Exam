# Generated by Django 4.1.4 on 2023-01-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCOOLAPP', '0027_matiere_surnommat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupe',
            name='CodeGroup',
        ),
        migrations.AlterField(
            model_name='groupe',
            name='nomGroup',
            field=models.CharField(default='GROUPE-', max_length=10, unique=True),
        ),
    ]
