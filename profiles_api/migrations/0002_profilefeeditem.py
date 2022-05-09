# Generated by Django 4.0.4 on 2022-05-09 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileFeedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
