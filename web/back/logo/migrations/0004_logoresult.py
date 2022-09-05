# Generated by Django 3.2.13 on 2022-08-16 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logo', '0003_auto_20220719_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FileField(null=True, upload_to='results/')),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logo.logo')),
            ],
        ),
    ]