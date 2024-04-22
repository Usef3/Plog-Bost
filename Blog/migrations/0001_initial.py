# Generated by Django 5.0.3 on 2024-04-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('bg_img', models.ImageField(upload_to='imges/%y/%m/%d')),
                ('created_ad', models.DateField(auto_now=True)),
                ('updated_ad', models.DateField(auto_now=True)),
            ],
        ),
    ]
