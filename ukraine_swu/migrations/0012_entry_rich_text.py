# Generated by Django 4.2.5 on 2023-11-13 13:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ukraine_swu', '0011_alter_entry_full_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='rich_text',
            field=ckeditor.fields.RichTextField(default='Text'),
        ),
    ]
