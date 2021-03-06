# Generated by Django 2.2.4 on 2019-09-13 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oritest', '0003_auto_20190912_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionnaireInstances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C1_score', models.IntegerField(default=0)),
                ('C2_score', models.IntegerField(default=0)),
                ('C3_score', models.IntegerField(default=0)),
                ('C4_score', models.IntegerField(default=0)),
                ('E1_score', models.IntegerField(default=0)),
                ('E2_score', models.IntegerField(default=0)),
                ('S1_score', models.IntegerField(default=0)),
                ('S2_score', models.IntegerField(default=0)),
                ('S3_score', models.IntegerField(default=0)),
                ('S4_score', models.IntegerField(default=0)),
                ('S5_score', models.IntegerField(default=0)),
                ('D1_score', models.IntegerField(default=0)),
                ('D2_score', models.IntegerField(default=0)),
                ('D3_score', models.IntegerField(default=0)),
                ('D4_score', models.IntegerField(default=0)),
                ('D5_score', models.IntegerField(default=0)),
                ('D6_score', models.IntegerField(default=0)),
                ('N1_score', models.IntegerField(default=0)),
                ('N2_score', models.IntegerField(default=0)),
                ('N3_score', models.IntegerField(default=0)),
                ('N4_score', models.IntegerField(default=0)),
                ('questionnaire_taken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oritest.Questionnaire')),
                ('taker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
