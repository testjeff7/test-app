# Generated by Django 4.0.6 on 2022-07-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image', verbose_name='Imagem')),
                ('titulo', models.TextField(blank=True, null=True, verbose_name='Titulo')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Texto')),
                ('link', models.TextField(verbose_name='Link')),
                ('button', models.TextField(verbose_name='Nome do botão')),
            ],
        ),
    ]