# Generated by Django 3.0.8 on 2020-07-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('date_released', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
