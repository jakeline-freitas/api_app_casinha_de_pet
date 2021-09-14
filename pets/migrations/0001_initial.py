# Generated by Django 3.2.7 on 2021-09-14 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pets.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id_pet', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('type', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=55)),
                ('vacinne', models.BooleanField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to=pets.models.upload_image_pet)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Responsável')),
            ],
        ),
    ]
