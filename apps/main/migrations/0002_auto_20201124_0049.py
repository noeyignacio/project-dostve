# Generated by Django 3.1.3 on 2020-11-23 16:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='^(09|\\+639)\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='category',
            field=models.CharField(choices=[('RNV', 'RNV'), ('LGU', 'LGU'), ('SME', 'SME'), ('Student', 'Student'), ('JCM', 'JCM'), ('Academe', 'Academe'), ('PWD', 'PWD'), ('General Public', 'General Public')], max_length=250),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='gender',
            field=models.CharField(choices=[('PREFER NOT TO SAY', 'PREFER NOT TO SAY'), ('OTHERS', 'OTHERS'), ('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=250),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
    ]
