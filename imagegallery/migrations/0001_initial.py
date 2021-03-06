# Generated by Django 2.2.1 on 2019-05-10 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('image_path', models.ImageField(upload_to='photos/')),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='imagegallery.Category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='imagegallery.Location')),
            ],
        ),
    ]
