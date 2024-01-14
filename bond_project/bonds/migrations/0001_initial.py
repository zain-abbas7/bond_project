# Generated by Django 5.0 on 2023-12-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bond_number', models.CharField(max_length=50)),
                ('draw_date', models.DateField()),
                ('denomination', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prize_won', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
