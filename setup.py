from setuptools import setup, find_packages

config = {
    'name': 'Libra',
    'version': '1.0',
    'author': 'Anonymous',
    'description': 'Static Analyzer for Certifying Fairness of Neural Networks',
    'license': 'MPL-2.0',
    'packages': find_packages('src'),
    'package_dir': {'': 'src'},
    'entry_points': {
             'console_scripts': [
                 'tool = tool.main:main',
                 ]
             },
    'install_requires': [
        'apronpy'
    ],
    'scripts': [],
}

setup(**config)
