# Generated by Django 2.1.4 on 2018-12-17 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(db_index=True, max_length=50)),
                ('book_img', models.FileField(null=True, upload_to='cover')),
                ('book_pdf', models.FileField(null=True, upload_to='pdf')),
                ('is_text', models.BooleanField(db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rps_name', models.CharField(max_length=30)),
                ('rps_pdf', models.FileField(upload_to='rps')),
            ],
        ),
        migrations.CreateModel(
            name='Usr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_name', models.CharField(max_length=30)),
                ('usr_pwd', models.CharField(max_length=30)),
                ('usr_grade', models.CharField(choices=[('A', 'Premium'), ('B', 'Regular'), ('C', 'Guest')], db_index=True, max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='rps',
            name='usr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cb.Usr'),
        ),
    ]
