# Generated by Django 3.0 on 2020-05-11 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal_area', '0003_auto_20200502_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_open',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.CharField(default='519555228', max_length=32, unique=True, verbose_name='name'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]