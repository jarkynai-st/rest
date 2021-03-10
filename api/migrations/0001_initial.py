# Generated by Django 3.1.7 on 2021-03-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('year', models.DateTimeField()),
                ('book_file', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
