# Generated by Django 3.1.7 on 2021-07-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FitnessClub_App', '0003_auto_20210712_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userspaymenthistory',
            name='Trainer_Name',
            field=models.CharField(max_length=33),
        ),
    ]
