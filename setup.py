from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'Python library leveraging REST Countries API to fetch and display country-specific data such as capitals, populations, currencies, and languages.'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="infokannegara",
    version=VERSION,
    author="apaya",
    author_email="<heyowassap@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='hhttps://github.com/codewithwan/infokannegara',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['info', 'negara'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)
