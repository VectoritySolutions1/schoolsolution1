# Generated by Django 2.2.1 on 2019-06-08 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20190605_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='classroom.Course'),
        ),
    ]
