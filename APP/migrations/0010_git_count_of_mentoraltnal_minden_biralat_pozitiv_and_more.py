# Generated by Django 4.1.2 on 2022-10-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0009_git_count_of_minden_biralat_pozitiv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='git',
            name='count_of_mentoraltnal_minden_biralat_pozitiv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='git',
            name='count_of_mentoraltnal_nincs_biralat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='git',
            name='count_of_mentoraltnal_nincs_mo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='git',
            name='count_of_mentoraltnal_nincs_repo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='git',
            name='count_of_mentoraltnal_van_negativ_biralat',
            field=models.IntegerField(default=0),
        ),
    ]