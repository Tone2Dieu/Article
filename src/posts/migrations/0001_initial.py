# Generated by Django 3.1.6 on 2023-11-01 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False, verbose_name='publié')),
                ('content', models.TextField(verbose_name='contenue')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Autheur')),
            ],
        ),
    ]
