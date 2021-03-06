# Generated by Django 3.2 on 2021-11-01 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GMF', '0007_auto_20211028_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('contact_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_json', models.TextField()),
                ('total_ammount', models.FloatField()),
                ('deliverd', models.BooleanField(default=False)),
                ('products', models.ManyToManyField(to='GMF.Products')),
            ],
        ),
        migrations.CreateModel(
            name='auth_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='avatar.jpg', upload_to='media')),
                ('phone', models.IntegerField()),
                ('address', models.ManyToManyField(to='GMF.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
