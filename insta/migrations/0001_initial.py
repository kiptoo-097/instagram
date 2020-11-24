# Generated by Django 3.1.3 on 2020-11-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('picture_name', models.CharField(max_length=50)),
                ('picture_caption', models.CharField(max_length=50)),
                ('likes', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]