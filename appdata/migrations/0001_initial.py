# Generated by Django 4.0.3 on 2022-05-21 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('aname', models.CharField(max_length=50)),
                ('aaname', models.CharField(max_length=50)),
                ('amt', models.CharField(max_length=50)),
                ('camt', models.CharField(max_length=50)),
                ('happy', models.CharField(max_length=50)),
                ('sad', models.CharField(max_length=50)),
                ('tot', models.CharField(max_length=50)),
            ],
        ),
    ]
