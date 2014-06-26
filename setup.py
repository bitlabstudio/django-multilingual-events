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
    'south',
    'django-countries==2.1.2',
    'django-hvad>=0.4',
    'django-document-library',
]

tests_require = [
    'fabric',
    'factory_boy',
    'django-nose',
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
    author_email='mbrochh@gmail.com',
    url="https://github.com/bitmazk/django-multilingnual-events",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='multilingual_events.tests.runtests.runtests',
)
