# Generated by Django 4.2.20 on 2025-03-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('rank', models.CharField(choices=[('IRON', 'Iron'), ('BRONZE', 'Bronze'), ('SILVER', 'Silver'), ('GOLD', 'Gold'), ('PLATINUM', 'Platinum'), ('DIAMOND', 'Diamond'), ('ASCENDANT', 'Ascendant'), ('IMMORTAL', 'Immortal'), ('RADIANT', 'Radiant')], default='IRON', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
    ]
