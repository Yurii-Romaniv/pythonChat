# Generated by Django 3.0.9 on 2023-12-08 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mkchat', '0015_auto_20231208_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
