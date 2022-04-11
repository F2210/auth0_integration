import re
import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='auth0_integration',
    version='1.0.4',
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    url='https://github.com/F2210/auth0_integration.git',
    author='Jacco Broeren',
    author_email='work@jaccobroeren.nl',
    maintainer="Jacco Broeren",
    maintainer_email="work@jaccobroeren.nl",
    python_requires='>=3.6, <4',
    install_requires=[
        'Django>=3.2', 'python-jose', 'sentry_sdk'
    ],
    packages=["auth0_integration"]
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        "Topic :: Internet :: WWW/HTTP",
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
    ],
)
