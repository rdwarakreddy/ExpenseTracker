# Generated by Django 4.2.1 on 2023-06-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('category', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
