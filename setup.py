#!/usr/bin/env python

from setuptools import setup

requirements = []  # add Python dependencies here
# e.g., requirements = ["PyYAML"]

setup(
    name='awx-custom-credential-plugin-cyberark',
    version='0.1',
    author='GSK',
    author_email='jeffrey.s.thorn@gsk.com',
    description='',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='https://github.com/spicoli9000/awx-custom-credential-plugin-example',
    packages=['awx_custom_credential_plugin_cyberark'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'jst_cyberark_plugin = awx_custom_credential_plugin_cyberark:jst_cyberark_plugin',
        ]
    }
)
