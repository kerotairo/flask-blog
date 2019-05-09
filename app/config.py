#Config variables for Flask App
import os
class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SQLALCEHMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR