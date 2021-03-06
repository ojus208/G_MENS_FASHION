# Generated by Django 3.2 on 2022-01-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GMF', '0011_products_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='sizes',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=500)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='size',
        ),
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.ManyToManyField(default='', to='GMF.sizes'),
        ),
    ]
