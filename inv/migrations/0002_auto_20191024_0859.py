# Generated by Django 2.2.5 on 2019-10-24 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fc',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='fm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Categoría', max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.Categoria')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sub Categorías',
                'unique_together': {('categoria', 'descripcion')},
            },
        ),
    ]
