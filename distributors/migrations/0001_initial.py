# Generated by Django 4.2.6 on 2023-10-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='distributors_images/', verbose_name='Фотография')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('region', models.CharField(choices=[('Баткен', 'Баткен'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Нарын', 'Нарын'), ('Ош', 'Ош'), ('Талас', 'Талас'), ('Чуй', 'Чуй')], max_length=50, verbose_name='Регион')),
                ('inn', models.IntegerField(unique=True, verbose_name='ИНН')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес по прописке')),
                ('actual_address', models.CharField(max_length=250, verbose_name='Фактическое место жительства')),
                ('passport_series', models.CharField(max_length=2, verbose_name='Серия паспорта')),
                ('passport_id', models.IntegerField(unique=True, verbose_name='Номер паспорта')),
                ('issued_by', models.CharField(max_length=255, verbose_name='Кем выдан')),
                ('issue_date', models.DateField(verbose_name='Дата выдачи')),
                ('validity', models.DateField(verbose_name='Срок действия')),
                ('contact1', models.IntegerField(verbose_name='Контактный номер один')),
                ('contact2', models.IntegerField(blank=True, null=True, verbose_name='Контактный номер два')),
                ('archived', models.BooleanField(default=True)),
            ],
        ),
    ]