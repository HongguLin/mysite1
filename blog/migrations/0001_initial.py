# Generated by Django 2.0.6 on 2018-06-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=128)),
                ('Password', models.CharField(max_length=128)),
                ('Email', models.CharField(max_length=128)),
                ('Firstname', models.CharField(max_length=128)),
                ('Lastname', models.CharField(max_length=128)),
            ],
        ),
    ]
