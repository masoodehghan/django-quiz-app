# Generated by Django 4.0.3 on 2022-05-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0008_marksofuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marksofuser',
            name='question',
        ),
        migrations.AddField(
            model_name='marksofuser',
            name='question',
            field=models.ManyToManyField(blank=True, null=True, to='testApp.question'),
        ),
    ]