# Generated by Django 2.2.2 on 2019-12-02 08:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_delete_tuplecopy'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuple',
            name='sump',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.CreateModel(
            name='UserPairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tuples', models.ManyToManyField(blank=True, null=True, to='core.Tuple')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pairs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
