# Generated by Django 5.2.1 on 2025-05-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210308_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
