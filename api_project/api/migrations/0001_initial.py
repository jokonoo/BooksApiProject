# Generated by Django 3.1.7 on 2021-10-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('published_date', models.CharField(max_length=128)),
                ('average_rating', models.IntegerField()),
                ('ratings_count', models.IntegerField()),
                ('thumbnail', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('books', models.ManyToManyField(to='api.Books')),
            ],
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('books', models.ManyToManyField(to='api.Books')),
            ],
        ),
    ]
