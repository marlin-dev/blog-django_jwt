# Generated by Django 2.1.7 on 2019-03-13 11:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0005_footer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Content',
            new_name='Article',
        ),
    ]
