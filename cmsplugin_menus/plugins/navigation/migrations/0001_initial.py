# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavMenu',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default=b'', help_text='Defaults to section page title if left blank.', max_length=255, verbose_name='menu title', blank=True)),
                ('collapse', models.BooleanField(default=False, help_text=b'Select this option if the menu should initially appear collapsed.', verbose_name='collapse menu')),
                ('section', models.ForeignKey(blank=True, to='cms.Page', help_text='Defaults to the root of current page if left blank.', null=True)),
            ],
            options={
                'verbose_name': 'Section Nav. Menu',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
