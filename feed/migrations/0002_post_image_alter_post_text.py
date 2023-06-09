# Generated by Django 4.2.1 on 2023-05-03 16:32

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=140),
        ),
    ]
