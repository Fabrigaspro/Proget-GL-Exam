# Generated by Django 4.1.4 on 2023-01-20 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCOOLAPP', '0015_professeur_descrptprof'),
    ]

    operations = [
        migrations.AddField(
            model_name='matiere',
            name='DescrptMat',
            field=models.CharField(default='Rien par rapport !', max_length=400),
        ),
        migrations.AddField(
            model_name='matiere',
            name='photoMat',
            field=models.ImageField(default=0, upload_to='photosCours/'),
            preserve_default=False,
        ),
    ]
