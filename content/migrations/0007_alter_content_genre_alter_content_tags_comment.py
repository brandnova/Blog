# Generated by Django 5.0.7 on 2024-07-15 22:59

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_alter_content_genre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='genres', to='content.genre'),
        ),
        migrations.AlterField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='content.tag'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='content.content')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='content.comment')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
