# Generated by Django 2.1.7 on 2019-05-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0003_auto_20190509_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaletters',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
