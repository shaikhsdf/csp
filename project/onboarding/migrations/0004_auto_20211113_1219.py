# Generated by Django 3.2.8 on 2021-11-13 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('onboarding', '0003_auto_20211111_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='doj',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='group',
            field=models.ForeignKey(blank=True, default=4, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='recruiter',
            field=models.CharField(default='R001', max_length=100),
        ),
    ]