from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='checkdown',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'checkdown': ['model/sign_classifier.tflite'],
    },
    install_requires=[
        'numpy>=1.19.2',
        'Pillow>=8.0.0',
        'tflite_runtime>=2.5.0',
    ],
    extras_require={
        'api': ['flask>=1.1.2'],
    },
    entry_points={
        'console_scripts': [
            'checkdown = checkdown.__main__:main',
        ],
    },
)