# Generated by Django 3.0.2 on 2020-02-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porto', '0004_liens'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fadein', models.CharField(max_length=50)),
                ('lien', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=None)),
                ('titre1', models.CharField(max_length=50)),
                ('titre2', models.CharField(max_length=50)),
                ('vue', models.IntegerField(blank=True, null=True)),
                ('aime', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'ProjectList',
                'verbose_name_plural': 'ProjectLists',
            },
        ),
    ]
