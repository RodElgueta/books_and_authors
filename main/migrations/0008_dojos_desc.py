# Generated by Django 3.2.5 on 2021-08-07 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_dojos_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='dojo antiguo', max_length=45),
        ),
    ]