# Generated by Django 2.0.1 on 2018-02-09 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('threads', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('thread', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='threads.Thread')),
            ],
        ),
        migrations.CreateModel(
            name='PollSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subjects', to='polls.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='votes', to='polls.Poll')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='votes', to='polls.PollSubject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
