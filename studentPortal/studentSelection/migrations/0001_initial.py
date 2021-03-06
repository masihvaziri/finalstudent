# Generated by Django 2.0.7 on 2018-07-16 05:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import studentSelection.extraTest.extra


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='allUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protest', models.TextField(null=True)),
                ('protestAnswer', models.TextField(null=True)),
                ('openProtest', models.BooleanField(default=True)),
                ('gradeValue', models.FloatField(null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='lessons',
            fields=[
                ('lessonID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('details', models.CharField(default='', max_length=50, null=True)),
                ('vahed', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('remain', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='myGrades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradeValue', models.FloatField(null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='selections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateReg', models.DateTimeField(max_length=30)),
                ('gradeValu', models.FloatField(null=True)),
                ('gradeFK', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='studentSelection.grades')),
                ('lessonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentSelection.lessons')),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('studentCode', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('status', models.IntegerField(null=True)),
                ('dateReg', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('img', studentSelection.extraTest.extra.ContentTypeRestrictedFileField(upload_to='images')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('teacherId', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('status', models.IntegerField(null=True)),
                ('dateReg', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('img', studentSelection.extraTest.extra.ContentTypeRestrictedFileField(upload_to='images')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='termDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('startTime', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='selections',
            name='studentCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentSelection.students'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='teacherID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentSelection.teacher'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentSelection.termDetails'),
        ),
        migrations.AddField(
            model_name='grades',
            name='lessonID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentSelection.lessons'),
        ),
        migrations.AddField(
            model_name='grades',
            name='studentCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentSelection.students'),
        ),
    ]
