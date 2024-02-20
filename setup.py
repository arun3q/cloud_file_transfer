from setuptools import setup, find_packages

setup(
    name='file_transfer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'google-cloud-storage',
    ],
)
