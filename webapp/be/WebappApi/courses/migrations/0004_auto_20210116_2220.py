# Generated by Django 3.1.5 on 2021-01-16 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210116_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentcategory',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='finalgrade',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='graduateattribute',
            name='outcome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.outcome'),
        ),
        migrations.AlterField(
            model_name='labexperience',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='lettergrade',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='section',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
