import os
from setuptools import setup, find_packages
import multilingual_events


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

install_requires = [
    'django',
    'django-cms',
    'django-countries',
    'django-hvad>=1.5.0',
    'django-document-library',
]

tests_require = [
    'fabric',
    'coverage',
    'django-coverage',
    'mock',
]

setup(
    name="django-multilingual-events",
    version=multilingual_events.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, event, i18n, hvad, multilingual, agenda, planning',
    author='Martin Brochhaus',
    author_email='martin.brochhaus@bitlabstudio.com',
    url="https://github.com/bitlabstudio/django-multilingual-events",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='multilingual_events.tests.runtests.runtests',
)
