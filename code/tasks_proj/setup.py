"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='tasks',
    version='0.1.0',
    license='proprietary',
    description='Minimal Project Task Management',

    author='Dinesh Sonachalam',
    author_email='Please use dineshsonachalam@gmail.com for contact.',
    url='',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['click', 'tinydb', 'six'],
    extras_require={'mongo': 'pymongo'},

    entry_points={
        'console_scripts': [
            'tasks = tasks.cli:tasks_cli',
        ]
    },
)
