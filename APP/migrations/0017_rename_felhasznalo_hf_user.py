# Generated by Django 4.0.2 on 2022-02-05 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0016_mo_szoveg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hf',
            old_name='felhasznalo',
            new_name='user',
        ),
    ]