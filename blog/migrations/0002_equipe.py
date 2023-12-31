# Generated by Django 3.2.22 on 2023-10-28 22:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('local', models.CharField(max_length=100)),
                ('membros', models.ManyToManyField(related_name='equipe_membros', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
