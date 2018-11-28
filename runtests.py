"""
A standalone test runner script, modified from pwned-passwords-django
"""

import os
import sys


# Make sure the app is (at least temporarily) on the import path.
APP_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, APP_DIR)


SETTINGS_DICT = {
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'django_transitive_dag',
        'tests'
    ),
    'ROOT_URLCONF': 'tests.urls',
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        },
    },
    'MIDDLEWARE': (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ),
}


def run_tests():
    # Making Django run this way is a two-step process. First, call
    # settings.configure() to give Django settings to work with:
    from django.conf import settings
    settings.configure(**SETTINGS_DICT)

    # Then, call django.setup() to initialize the application registry
    # and other bits:
    import django
    django.setup()

    # Now we instantiate a test runner...
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)

    # And then we run tests and return the results.
    test_runner = TestRunner(verbosity=2, interactive=True)
    failures = test_runner.run_tests(['tests'])
    sys.exit(failures)


if __name__ == '__main__':
    run_tests()
