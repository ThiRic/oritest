# Generated by Django 2.2.4 on 2019-09-13 07:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oritest', '0004_questionnaireinstances'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionnaireInstances',
            new_name='QuestionnaireInstance',
        ),
    ]
