from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='weathercli',
    version='2.3.1',
    author='Brian Riley',
    author_email='brian@btriley.com',
    description="A command line weather tool",
    url='https://github.com/brianriley/weather-cli',
    py_modules=['weathercli'],
    long_description=read('README.mkd'),
    install_requires=['clint==0.3.4'],
    entry_points={
        'console_scripts': [
            'weather = weathercli:Weather.main',
            ],
        },
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
