# Generated by Django 2.1.7 on 2019-05-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190507_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificacao',
            name='prefixo',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]