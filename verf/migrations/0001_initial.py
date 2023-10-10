# Generated by Django 4.2.5 on 2023-10-08 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import verf.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('ref_code', models.CharField(default=verf.models.generate_ref, max_length=6, unique=True)),
                ('referrer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referrals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]