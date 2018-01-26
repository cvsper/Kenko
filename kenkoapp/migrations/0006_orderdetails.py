# Generated by Django 2.0.1 on 2018-01-24 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kenkoapp', '0005_auto_20180124_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('care', models.ForeignKey(on_delete='on_delete', to='kenkoapp.Care')),
                ('order', models.ForeignKey(on_delete='on_delete', related_name='order_details', to='kenkoapp.Order')),
            ],
        ),
    ]