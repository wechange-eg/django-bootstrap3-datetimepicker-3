import sys
from setuptools import setup

long_description = ''
if 'upload' in sys.argv or 'register' in sys.argv:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='django-bootstrap3-datetimepicker-3',
    packages=['bootstrap3_datetime'],
    include_package_data=True,
    version='2.6.0',
    description='Bootstrap3 compatible datetimepicker for Django 1.11 projects.',
    long_description=long_description,
    author='Nakahara Kunihiko/Samuel Colvin/Neil Clayton',
    author_email='nakahara.kunihiko@gmail.com/s@muelcolvin.com/neil@shinywhitebox.com',
    url='https://github.com/shinywhitebox/django-bootstrap3-datetimepicker',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
