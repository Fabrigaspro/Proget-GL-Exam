# Generated by Django 4.1.4 on 2023-01-28 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SCOOLAPP', '0032_remove_bulletindenote_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletindenote',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SCOOLAPP.eleve', unique=True),
        ),
    ]