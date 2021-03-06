# Generated by Django 3.2.5 on 2021-07-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_bank_mandate_mandatecollection_mandatecollectionbatch_mandatecollectionbatchcollections_mandatecolle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id_type', models.IntegerField(blank=True, null=True)),
                ('id_value', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('principal_uid', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerBankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'customer_bank_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerBankAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'customer_bank_accounts',
                'managed': False,
            },
        ),
    ]
