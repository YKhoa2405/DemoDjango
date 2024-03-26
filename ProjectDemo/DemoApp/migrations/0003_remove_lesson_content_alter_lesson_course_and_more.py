# Generated by Django 5.0.2 on 2024-03-03 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0002_tag_course_image_alter_user_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='content',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='DemoApp.course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='DemoApp.tag'),
        ),
    ]