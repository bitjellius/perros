# Generated by Django 2.1.2 on 2018-10-25 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rescate', '0002_auto_20181025_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='perrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePerro', models.CharField(blank=True, max_length=50)),
                ('razaP', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('imagen', models.ImageField(upload_to='')),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rescate.Estado')),
            ],
        ),
    ]
