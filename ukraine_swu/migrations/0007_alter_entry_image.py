# Generated by Django 4.1.1 on 2023-11-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukraine_swu', '0006_alter_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.TextField(default='https://media.sproutsocial.com/uploads/2017/02/10x-featured-social-media-image-size.png'),
        ),
    ]
