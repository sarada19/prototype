# Generated by Django 4.1.1 on 2022-09-06 22:46

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
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('file', models.FileField(upload_to='File')),
                ('status', models.BooleanField(default=False, verbose_name='Approved')),
                ('date_asked', models.DateField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.TextField()),
                ('file', models.FileField(upload_to='Answers')),
                ('staus', models.BooleanField(default='False')),
                ('ate_answered', models.DateField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.users')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.post')),
            ],
        ),
    ]
