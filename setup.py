from setuptools import setup, find_packages

setup(
    name='DNSwitch',
    scripts=['DNSwitch'],
    version='1.0',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "nserver"
    ]
)