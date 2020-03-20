# Generated by Django 2.2.10 on 2020-03-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0003_auto_20200318_0038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainmessage',
            options={'ordering': ['create_time'], 'verbose_name': '留言', 'verbose_name_plural': '留言'},
        ),
        migrations.AlterModelOptions(
            name='replymessage',
            options={'ordering': ['create_time'], 'verbose_name': '留言回复', 'verbose_name_plural': '留言回复'},
        ),
        migrations.AddField(
            model_name='message',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
    ]