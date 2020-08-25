# Generated by Django 2.2 on 2020-08-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='name',
        ),
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='publisher',
            name='first_name',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='publisher',
            name='last_name',
            field=models.CharField(default='', max_length=45),
        ),
    ]