# Generated by Django 3.1.7 on 2021-03-15 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books.genre'),
            preserve_default=False,
        ),
    ]
