# Generated by Django 5.0.1 on 2024-01-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('url', models.ImageField(upload_to='cat_images')),
            ],
            options={
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='cats_cat_created_75a26b_idx')],
            },
        ),
    ]
