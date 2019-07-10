# Generated by Django 2.2.1 on 2019-07-10 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='APK_UPLOADFILE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=None, verbose_name='用户id')),
                ('username', models.CharField(default=None, max_length=10, verbose_name='用户名')),
                ('name_des', models.CharField(max_length=50, verbose_name='名称描述')),
                ('apk_testtype', models.CharField(max_length=200, verbose_name='测试类型')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('upfilepath', models.FileField(upload_to='')),
                ('sum_status', models.IntegerField(default=0, verbose_name='运行状态')),
                ('sum_result', models.IntegerField(default=0, verbose_name='运行结果')),
                ('del_status', models.IntegerField(default=0, verbose_name='是否删除')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.Module')),
            ],
            options={
                'verbose_name': 'apk管理_文件上传',
                'verbose_name_plural': 'apk管理_文件上传',
            },
        ),
        migrations.CreateModel(
            name='APK_RESULTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=None, verbose_name='用户id')),
                ('username', models.CharField(default=None, max_length=10, verbose_name='用户名')),
                ('name_des', models.CharField(max_length=50, verbose_name='名称描述')),
                ('apk_testtype', models.CharField(max_length=200, verbose_name='测试类型')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('upfilepath', models.FileField(upload_to='', verbose_name='上传zip和apk文件路徑')),
                ('apkfile_path', models.FileField(upload_to='', verbose_name='apk文件路徑')),
                ('run_status', models.IntegerField(default=0, verbose_name='运行状态')),
                ('run_result', models.IntegerField(default=0, verbose_name='运行结果')),
                ('del_status', models.IntegerField(default=0, verbose_name='是否删除')),
                ('detail', models.CharField(max_length=1000, verbose_name='运行结果')),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apk.APK_UPLOADFILE')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.Module')),
            ],
            options={
                'verbose_name': 'apk管理_运行结果',
                'verbose_name_plural': 'apk管理_运行结果',
            },
        ),
    ]
