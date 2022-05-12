# Generated by Django 3.2 on 2021-10-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('mrp', models.FloatField()),
                ('off', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('color', models.CharField(max_length=20)),
                ('size_available', models.TextField()),
                ('quantity', models.IntegerField()),
                ('category', models.TextField()),
            ],
        ),
    ]