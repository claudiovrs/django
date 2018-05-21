# Generated by Django 2.0.3 on 2018-05-16 01:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20180515_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sessao',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2803ced3-99bf-4d70-a3f3-70b52ef6759c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]