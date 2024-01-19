# Generated by Django 3.2.10 on 2024-01-18 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20240118_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languageName', models.TextField()),
                ('mcqId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mcqlistdatatmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TopicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicName', models.TextField()),
                ('languageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.languagemodel')),
            ],
        ),
    ]
