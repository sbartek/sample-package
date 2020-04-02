import os
import sys

from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, 'src')
sys.path.insert(0, src_dir)

import samplePackage

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='samplePackage',
    version=samplePackage.__version__,
    description='Sample Python Package',
    author='bartek',
    author_email='bartekskorulski@gmail.com',
    packages=find_packages(where='src', exclude=['tests']),
    package_dir={'': 'src'},
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    testsp_require=get_requirements('requirements.test.txt'),
    url='https://github.com/sbartek/sample-package',
    classifiers=[
        'Programming Language :: Python :: 3.7.7'
    ],
)
