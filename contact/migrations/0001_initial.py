# Generated by Django 2.2 on 2019-07-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=35)),
                ('iage', models.IntegerField()),
                ('iemail', models.CharField(max_length=35)),
                ('imsg', models.CharField(max_length=1000)),
            ],
        ),
    ]
