# Generated by Django 3.1.7 on 2021-05-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkchat', '0012_auto_20210529_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
        migrations.AddField(
            model_name='users',
            name='hashedpasword',
            field=models.CharField(default='827ccb0eea8a706c4c34a16891f84e7b', max_length=32, verbose_name='хеш'),
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default='827ccb0eea8a706c4c34a16891f84e7b', max_length=32, verbose_name='токен'),
        ),
    ]