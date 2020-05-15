# Generated by Django 3.0 on 2020-05-11 23:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal_area', '0004_auto_20200512_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DepositType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('percent', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.CharField(default='988586858', max_length=32, unique=True),
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_area.DepositType')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_open', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_sum', models.IntegerField()),
                ('loan', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_area.CreditType')),
            ],
        ),
    ]