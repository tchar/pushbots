try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from codecs import open
from os import path

current_dir = path.abspath(path.dirname(__file__))

try:
    from pypandoc import convert

    def read_md(f): return convert(path.join(current_dir, f), 'rst')

except ImportError:
    print('Warning: pypandoc module not found, could not convert ,'
          ' Markdown to RST')

    def read_md(f): return open(path.join(current_dir, f), 'r').read()


setup(
    name='pushbots',

    version='0.0.1',

    description='REST API library for pushbots.',
    long_description=read_md('README.md'),

    # The project's main homepage.
    url='https://github.com/tchar/pushbots',

    # Author details
    author='Tilemachos Charalampous',
    author_email='tilemachos.charalampous@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        # Project intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # License
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions supported.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],

    # What does the project relate to?
    keywords='pushbots, push, push notifications, gcm, google cloud messaging',

    # Packages included
    packages=['pushbots', 'pushbots.tests'],

    install_requires=['requests'],

    # Other package data
    include_package_data=True,
    package_data={
        'examples': [
            'examples/alias.py',
            'examples/analytics.py',
            'examples/generic.py',
            'examples/get_token_from_alias.py',
            'examples/location.py',
            'examples/push_batch.py',
            'examples/tag_untag.py',
            'examples/unregister.py',
            ],
    },
)
