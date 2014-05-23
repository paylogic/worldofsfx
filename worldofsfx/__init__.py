#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_environments import Environments

from worldofsfx.database import db

from worldofsfx.wos.views import wos
from worldofsfx.events.views import events
from worldofsfx.buzz.views import buzz


def create_app(environment="DEVELOPMENT"):
    """worldofsfx application factory.

    This function defines a re-usable pattern for instantiating and creating
    application objects.

    :param str environment: Specify the name of the configuration object used
                            to build this application object

    Usage::
        from worldofsfx import create_app
        from unittest import TestCase

        class MyTest(TestCase):

            def setUp(self):
                self.app = create_app(environment="TESTING")

    :returns: flask application
    :rtype: :obj:`flask.Flask`
    """
    app = Flask(__name__)
    env_name = environment.upper()
    env = Environments(app, default_env=env_name)
    env.from_object('worldofsfx.config')

    app.template_folder = app.config.get('TEMPLATE_FOLDER', 'templates')

    app.register_blueprint(wos)
    app.register_blueprint(events)
    app.register_blueprint(buzz)

    db.init_app(app)

    return app
