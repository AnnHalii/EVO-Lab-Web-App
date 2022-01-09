# Generated by Django 3.2.7 on 2022-01-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddIndex(
            model_name='additionaldata',
            index=models.Index(fields=['email'], name='user_app_ad_email_096196_idx'),
        ),
    ]
