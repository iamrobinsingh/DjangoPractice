# Generated by Django 2.1.15 on 2020-06-27 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApplication', '0002_contactinfos_student1_teacher1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop1', models.CharField(max_length=128)),
                ('prop2', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Parent1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop1', models.CharField(max_length=128)),
                ('prop2', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Parent2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop3', models.CharField(max_length=128)),
                ('prop4', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('parent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testApplication.Parent')),
                ('prop3', models.CharField(max_length=128)),
                ('prop4', models.CharField(max_length=128)),
            ],
            bases=('testApplication.parent',),
        ),
        migrations.CreateModel(
            name='SubChild',
            fields=[
                ('child_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testApplication.Child')),
                ('prop5', models.CharField(max_length=128)),
            ],
            bases=('testApplication.child',),
        ),
    ]
