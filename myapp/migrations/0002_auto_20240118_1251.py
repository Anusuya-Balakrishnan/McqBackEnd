# Generated by Django 3.2.10 on 2024-01-18 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicmodel',
            name='languageId',
        ),
        migrations.DeleteModel(
            name='LanguageModel',
        ),
        migrations.DeleteModel(
            name='TopicModel',
        ),
    ]