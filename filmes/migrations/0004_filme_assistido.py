# Generated by Django 5.0.3 on 2024-04-08 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0003_alter_filme_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='assistido',
            field=models.BooleanField(default='False'),
        ),
    ]
