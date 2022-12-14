# Generated by Django 4.1.1 on 2022-10-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='choice_text',
            new_name='answer_text',
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.IntegerField(choices=[(1, 'open'), (2, 'closed')], default=1),
        ),
    ]
