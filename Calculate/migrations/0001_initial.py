# Generated by Django 3.0.2 on 2020-02-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(null=True)),
                ('y', models.IntegerField(null=True)),
                ('operator', models.CharField(max_length=2000, null=True)),
                ('result', models.IntegerField(null=True)),
            ],
        ),
    ]
