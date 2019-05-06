"""A setuptools based setup module for devmgr"""
from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'flask',
    'flask-restful',
    'flask-sqlalchemy',
    'flask-marshmallow',
    'marshmallow-sqlalchemy',
    'python-dotenv'
]

test_requirements = [
    'pytest',
]

setup(
    name='devmgr',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Device management application",
    long_description=readme + '\n\n' + history,
    author="Tong Jiang",
    author_email='tong.jiang@gmail.com',
    url='https://github.com/jnpr-tjiang/devmgr',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        'dotenv': ['python-dotenv'],
        'dev': [
            'pytest>=3',
            'coverage',
            'tox',
            'flake8'
        ]
    },
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'devmgr=devmgr.cli:cli',
        ],
    },
)
