# Generated by Django 2.0.6 on 2018-06-27 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20180623_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='oranization',
            new_name='organization',
        ),
        migrations.AddField(
            model_name='professor',
            name='image',
            field=models.ImageField(default='/dd', upload_to='web/posts/title/image'),
        ),
        migrations.AddField(
            model_name='professor',
            name='state',
            field=models.CharField(default='.', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
