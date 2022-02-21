# Generated by Django 3.1.4 on 2022-01-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'verbose_name': 'Доска', 'verbose_name_plural': 'Доска'},
        ),
        migrations.AddField(
            model_name='art',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/blog/%Y/%m/%d', verbose_name='Ссылка картинки'),
        ),
        migrations.AlterField(
            model_name='art',
            name='full_text',
            field=models.TextField(verbose_name='статья'),
        ),
    ]
