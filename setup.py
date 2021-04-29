from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.2.3'
DESCRIPTION = 'Set up a Python Discord bot quickly!'
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="botPlus",
    version=VERSION,
    author="OreoDivision",
    author_email="<bobgim20@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['discord.py', 'colorama'],
    keywords=['python', 'discord', 'discord.py', 'bot', 'discord bot', 'quick'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)