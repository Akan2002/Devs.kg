# Generated by Django 3.2.7 on 2023-02-08 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vakanci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Нахвание')),
                ('job_title', models.CharField(max_length=120, verbose_name='Должность')),
                ('salary', models.CharField(max_length=200, verbose_name='Оклад')),
                ('type', models.CharField(max_length=127, verbose_name='Тип')),
                ('description', models.TextField(verbose_name='Описание')),
                ('email', models.EmailField(max_length=254, verbose_name='Емаил')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vakancies', to='company.company')),
            ],
            options={
                'verbose_name': 'Ваканксия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
