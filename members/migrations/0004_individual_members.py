# Generated by Django 1.11.dev20161105150738 on 2016-11-08 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0003_corporatemember_django_usage_verbose_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DeveloperMember",
            new_name="IndividualMember",
        ),
    ]
