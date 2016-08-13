from distutils.core import setup
from setuptools import find_packages

setup(
    name='SpotiPy',
    version='1.0.0',
    scripts=['SpotiPy'],
    packages=find_packages(exclude=['tests*']),
    license='WTFPL',
    description='Spotify player using Python and AppleScript',
    long_description='Spotify player using Python and AppleScript',
    # install_requires=[''],
    url='http://github.com/ariestiyansyah/SpotiPy',
    author='Rizky Ariestiyansyah',
    author_email='ariestiyansyah.rizky@gmail.com'
)
