# Generated by Django 3.0 on 2022-02-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0008_auto_20220208_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'emp',
            },
        ),
    ]
