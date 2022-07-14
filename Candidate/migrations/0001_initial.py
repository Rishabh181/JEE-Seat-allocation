# Generated by Django 3.0a1 on 2020-03-10 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=50)),
                ('preferences', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollnumber', models.CharField(max_length=15, unique=True)),
                ('category', models.CharField(choices=[('GEN', 'GEN'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('GENPWD', 'GENPWD'), ('OBCPWD', 'OBCPWD'), ('SCPWD', 'SCPWD'), ('STPWD', 'STPWD')], max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=100)),
                ('rank', models.IntegerField(unique=True)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('preferences', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('final_seat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Candidate.Branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Candidate.College'),
        ),
    ]
