# Generated by Django 5.0.1 on 2024-02-18 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_student_id_alter_teacher_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]