# Generated by Django 2.2.10 on 2020-06-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_index=True, max_length=256, verbose_name='Название'),
        ),
    ]
