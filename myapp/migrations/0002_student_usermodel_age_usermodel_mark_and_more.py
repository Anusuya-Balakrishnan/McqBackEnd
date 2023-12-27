# Generated by Django 4.1.13 on 2023-12-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date', models.DateField()),
                ('dob', models.DateField()),
                ('mobileNumber', models.IntegerField()),
                ('address', models.TextField()),
                ('qualification', models.TextField()),
                ('nationality', models.TextField()),
                ('workingDesignation', models.TextField()),
                ('studentCollegeName', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('whatsappNumber', models.IntegerField()),
                ('gender', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='usermodel',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='mark',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='username',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
