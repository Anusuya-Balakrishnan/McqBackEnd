# Generated by Django 3.2.10 on 2024-01-29 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answeredQuestions', djongo.models.fields.JSONField()),
                ('result', models.IntegerField()),
                ('level', models.TextField()),
                ('languageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.languagemodel')),
                ('topicId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.topicmodel')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
