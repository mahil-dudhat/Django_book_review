# Generated by Django 3.2.6 on 2022-04-29 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='public_book_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=50)),
                ('book_image', models.TextField(max_length=50)),
                ('book_author', models.TextField()),
            ],
        ),
    ]
