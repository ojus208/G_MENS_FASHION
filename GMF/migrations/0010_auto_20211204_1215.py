# Generated by Django 3.2 on 2021-12-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMF', '0009_auto_20211105_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ManyToManyField(to='GMF.images'),
        ),
    ]
