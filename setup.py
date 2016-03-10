from setuptools import setup, find_packages

setup(
    name='ppr',
    description='Python project generation tool.',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        ppr=ppr.cli:cmd_ppr
    ''',
)
