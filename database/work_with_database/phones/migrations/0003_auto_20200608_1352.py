# Generated by Django 2.2.10 on 2020-06-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20200608_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(verbose_name=models.CharField(db_index=True, default=None, max_length=20)),
        ),
    ]
