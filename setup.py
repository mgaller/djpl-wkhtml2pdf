#! /usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='djpl-wkhtml2pdf',
    version='0.1',
    description='A simple wrapper around wkhtml2pdf',
    long_description=read('README.rst'),
    license='The MIT License',
    keywords='django, django-productline, pdf export, wkhtml2pdf',
    author='Toni Michel',
    author_email='toni.michel@schnapptack.de',
    url="https://github.com/tonimichel/djpl-wkhtml2pdf",
    packages=find_packages(),
    package_dir={'wkhtml2pdf': 'wkhtml2pdf'},
    include_package_data=True,
    scripts=[],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        
    ]
)
