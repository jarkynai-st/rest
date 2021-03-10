# Generated by Django 3.1.7 on 2021-03-09 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210309_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('email', 'email'), ('phone', 'phone'), ('address', 'address')], max_length=40)),
                ('info', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.branch')),
            ],
        ),
    ]