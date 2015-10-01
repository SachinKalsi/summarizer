# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages

version = ''
with open('summarizer/__init__.py', 'r') as fp:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fp.read(),
        re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("Cannot find version information")

with open('README.md', 'r') as fp:
    readme = fp.read()
with open('CHANGES.md', 'r') as fp:
    changes = fp.read()
with open('LICENSE.md', 'r') as fp:
    license = fp.read()

setup(
    name='summarizer',
    version=version,
    description='A text summarizer',
    long_description=readme + '\n\n' + changes,
    author='Eric Bower',
    author_email='neurosnap@gmail.com',
    url='https://github.com/michigan-com/summarizer',
    packages=find_packages(),
    package_data={'summarizer': ['trainer/*.txt', 'trainer/*.json']},
    include_package_data=True,
    install_requires=['nltk'],
    license=license,
    classifiers=(
        b'Development Status :: 3 - Alpha',
        b'Environment :: Console',
        b'Intended Audience :: Developers',
        b'License :: OSI Approved :: MIT License',
        b'Natural Language :: English',
        b'Programming Language :: Python :: 2.7',
        b'Programming Language :: Python :: 3.4',
        b'Topic :: Text Editors :: Text Processing',
    ),
)
