# Generated by Django 4.2.5 on 2023-11-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukraine_swu', '0008_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='entry',
            name='full_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]