# Generated by Django 5.0.7 on 2024-07-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_subscription_delete_newslettersubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
