# Generated by Django 4.0.2 on 2022-04-18 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngosignup', '0002_alter_ngosignup_image_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='USERS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_name', models.CharField(max_length=256)),
                ('req_email', models.EmailField(max_length=256)),
                ('req_password', models.CharField(max_length=256)),
                ('req_phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('age', models.DecimalField(decimal_places=0, max_digits=5)),
                ('domain', models.CharField(max_length=10)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='static/images/userspic')),
                ('agree', models.BooleanField()),
            ],
        ),
    ]
