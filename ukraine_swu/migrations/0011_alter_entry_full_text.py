# Generated by Django 4.2.5 on 2023-11-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukraine_swu', '0010_alter_entry_full_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='full_text',
            field=models.TextField(),
        ),
    ]
