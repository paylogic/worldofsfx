from os import path

"""
    worldofsfx configuration objects.

    Define custom config objects here or update existing ones.  Configuration objects
    will be picked up by either defining a FLASK_ENV eviornment variable or by explicitly
    passing the upper case class name to the application factory.

    Useage::

        class MyConfig(config):

            S3_URL = "https://s3.amazon.com/foo/bar

        >>> from worldofsfx import create_app
        >>> create_app(environment="MYCONFIG")
"""


class Config(object):
    DEBUG = False
    PORT = 5000
    HOST = "0.0.0.0"
    SQLALCHEMY_ECHO = True
    BASE_URL = "http://worldofsfx.com"
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    TEMPLATE_FOLDER = path.join(PROJECT_ROOT, 'templates')
    BEATPORT_API_USERNAME="your-beatport-api-username"
    BEATPORT_API_PASSWORD="your-beatport-api-password"

class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://{{ DB_USER }}:{{ DB_PASS }}@localhost/{{ DB_NAME }}"
    SECRET_KEY = "c1893e25-88ec-4ec2-b2fe-4c213413df25"


class Stage(Config):
    DEBUG = True


class Production(Config):
    SQLALCHEMY_ECHO = False
    DEBUG = True


class Testing(Config):
    SECRET_KEY = "2147d2df-759b-40ac-8013-f6154110a7d0"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://{{ DB_USER }}:{{ DB_PASS }}@localhost/{{DB_NAME}}_test"
    SQLALCHEMY_ECHO = False
