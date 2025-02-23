# Generated by Django 5.1 on 2024-11-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_datos_encap_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='lag_administrative_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datos',
            name='encap_type',
            field=models.CharField(choices=[('N/A', 'N/A'), ('dot1q', 'dot1q'), ('qinq', 'qinq')], default='N/A', max_length=100),
        ),
    ]
