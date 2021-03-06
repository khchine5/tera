# -*- coding: UTF-8 -*-
# Copyright 2014-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""
Base Django settings for Lino Tera applications.

"""

from __future__ import print_function
from __future__ import unicode_literals

from lino.projects.std.settings import *
from lino.api.ad import _
from lino_tera import SETUP_INFO

class Site(Site):

    verbose_name = "Lino Tera"
    version = SETUP_INFO['version']
    url = "http://tera.lino-framework.org/"

    demo_fixtures = 'std minimal_ledger demo demo2'.split()
    # demo_fixtures = 'std demo minimal_ledger euvatrates demo2'.split()

    # project_model = 'tera.Client'
    project_model = 'courses.Course'
    # project_model = 'contacts.Partner'
    textfield_format = 'html'
    user_types_module = 'lino_tera.lib.tera.user_types'
    workflows_module = 'lino_tera.lib.tera.workflows'
    custom_layouts_module = 'lino_tera.lib.tera.layouts'
    obj2text_template = "**{0}**"

    default_build_method = 'appyodt'
    
    # experimental use of rest_framework:
    # root_urlconf = 'lino_book.projects.team.urls'
    
    # migration_class = 'lino_tera.lib.tera.migrate.Migrator'

    auto_configure_logger_names = "atelier django lino lino_xl lino_tera"

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        # yield 'lino.modlib.users'
        yield 'lino_tera.lib.users'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.properties'
        yield 'lino_tera.lib.contacts'
        yield 'lino_tera.lib.households'
        yield 'lino_xl.lib.clients'
        yield 'lino_xl.lib.phones'
        # yield 'lino_tera.lib.lists'
        # yield 'lino_xl.lib.beid'
        # yield 'lino_xl.lib.addresses'
        yield 'lino_xl.lib.humanlinks',
        yield 'lino_tera.lib.products'
        yield 'lino_tera.lib.sales'
        yield 'lino_tera.lib.courses'
        # yield 'lino_xl.lib.accounts'
        # yield 'lino_xl.lib.vat'
        yield 'lino_xl.lib.sepa'
        yield 'lino_xl.lib.finan'
        yield 'lino_xl.lib.invoicing'
        yield 'lino_xl.lib.bevats'
        yield 'lino_xl.lib.ana'
        # 'lino_xl.lib.projects',
        # yield 'lino_xl.lib.blogs'
        yield 'lino_xl.lib.topics'
        yield 'lino_xl.lib.notes'
        # yield 'lino_tera.lib.tickets'
        # yield 'lino_xl.lib.skills'
        # yield 'lino_xl.lib.votes'
        # yield 'lino_tera.lib.working'
        # yield 'lino_xl.lib.deploy'
        # yield 'lino_presto.lib.working'
        # yield 'lino.modlib.uploads'
        # yield 'lino_xl.lib.extensible'
        yield 'lino_xl.lib.cal'
        # yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.excerpts'
        yield 'lino_xl.lib.appypod'
        # yield 'lino_xl.lib.postings'
        # yield 'lino_xl.lib.pages'

        yield 'lino.modlib.export_excel'
        yield 'lino.modlib.checkdata'
        yield 'lino.modlib.tinymce'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.weasyprint'

        yield 'lino_tera.lib.tera'
        yield 'lino_tera.lib.teams'
        yield 'lino_xl.lib.lists'

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(country_code='BE')
        # self.plugins.working.configure(ticket_model='contacts.Person')
        # self.plugins.skills.configure(demander_model='contacts.Person')
        self.plugins.topics.configure(partner_model='courses.Course')
        # self.plugins.coachings.configure(client_model='tera.Client')
        self.plugins.clients.configure(client_model='contacts.Partner')
        self.plugins.countries.configure(hide_region=True)
        self.plugins.countries.configure(country_code='BE')
        self.plugins.ledger.configure(start_year=2015)
        self.plugins.ledger.configure(use_pcmn=True)
        # self.plugins.courses.configure(teacher_model='users.User')
        # self.plugins.courses.configure(pupil_model='contacts.Person')
        self.plugins.courses.configure(pupil_model='tera.Client')


    # def setup_actions(self):
    #     from lino.core.merge import MergeAction
    #     lib = self.models
    #     for m in (lib.contacts.Company, lib.tera.Client,
    #               lib.contacts.Person,
    #               lib.households.Household,
    #               lib.countries.Place):
    #         m.define_action(merge_row=MergeAction(m))
    #     super(Site, self).setup_actions()

# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'

USE_TZ = True
# TIME_ZONE = 'Europe/Brussels'
# TIME_ZONE = 'Europe/Tallinn'
TIME_ZONE = 'UTC'

