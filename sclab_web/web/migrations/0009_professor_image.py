# Generated by Django 2.0.6 on 2018-06-27 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_professor_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='image',
            field=models.ImageField(default='/dd', upload_to='web/posts/title/image'),
        ),
    ]
