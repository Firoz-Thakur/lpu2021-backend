# Generated by Django 3.2.7 on 2021-09-29 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_user_id'),
        ('entries', '0006_alter_entry_returns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
