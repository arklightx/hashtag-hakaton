# Generated by Django 3.2.7 on 2021-10-08 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.courses', verbose_name='Курс'),
        ),
    ]