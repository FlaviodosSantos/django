# Generated by Django 3.2.4 on 2021-08-02 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20210801_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('impostos', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
