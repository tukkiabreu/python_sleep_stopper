from setuptools import setup, find_packages

import sleep_stopper

setup(
    name='sleep_stopper',
    version=sleep_stopper.__version__,
    author=sleep_stopper.__author__,
    author_email='arthurabreu@id.uff.br',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'sleep_stopper=sleep_stopper.script:run_program'
        ]
    }
)
