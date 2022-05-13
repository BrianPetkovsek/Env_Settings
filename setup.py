from setuptools import setup

import os
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup(
    name='Env_Settings',
    version='0.0.1',
    description='Env_Settings',
    url='git@github.com:BrianPetkovsek/Env_Settings.git',
    author='Brian Petkovsek',
    author_email='contactnorthedgecomputers@gmail.com',
    license='unlicense',
    packages=['Env_Settings'],
	install_requires=install_requires,
    zip_safe=False
)