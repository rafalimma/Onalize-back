# Generated by Django 5.1.7 on 2025-03-22 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ona', '0004_emailtalks_hash_id_emailtalks_origem_emailtalks_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='cidade',
            new_name='estado',
        ),
        migrations.RemoveField(
            model_name='emailtalks',
            name='tipo',
        ),
        migrations.AddField(
            model_name='employee',
            name='senioridade',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
