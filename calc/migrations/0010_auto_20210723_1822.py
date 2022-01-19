# Generated by Django 3.2.4 on 2021-07-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_fooddata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YearlySales',
            new_name='WeeklySales',
        ),
        migrations.RenameField(
            model_name='weeklysales',
            old_name='yearly',
            new_name='weekly',
        ),
        migrations.AlterField(
            model_name='fooddata',
            name='price',
            field=models.FloatField(),
        ),
    ]