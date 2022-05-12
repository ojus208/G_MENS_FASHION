# Generated by Django 3.2 on 2022-01-21 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GMF', '0012_auto_20220119_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sizes',
            name='stock',
        ),
        migrations.CreateModel(
            name='sizes_stock',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('stock', models.IntegerField(default=0)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GMF.sizes')),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.ManyToManyField(default='', to='GMF.sizes_stock'),
        ),
    ]
