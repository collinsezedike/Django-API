# Generated by Django 4.0.5 on 2022-07-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_alter_link_created_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='created_data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
