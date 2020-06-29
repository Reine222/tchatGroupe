# Generated by Django 2.2.8 on 2020-06-26 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='avatar')),
                ('contact', models.CharField(max_length=250)),
                ('lien_fb', models.URLField()),
                ('lien_twt', models.URLField()),
                ('lien_insta', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profileUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_post', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auteurMessage', to='kozer.Profile')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]