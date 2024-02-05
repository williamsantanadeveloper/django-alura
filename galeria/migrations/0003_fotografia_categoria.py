# Generated by Django 5.0.1 on 2024-02-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_rename_photo_fotografia_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
