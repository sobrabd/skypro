# Generated by Django 4.2 on 2023-04-11 14:51

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
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('experience', models.TextField(max_length=255)),
                ('portfolio', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
