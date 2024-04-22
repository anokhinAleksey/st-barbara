# Generated by Django 5.0.3 on 2024-04-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('text_en', models.TextField(null=True)),
                ('text_uk', models.TextField(null=True)),
                ('text_ru', models.TextField(null=True)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]