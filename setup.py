import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="myfoo",
    version="1.0",
    author="winway",
    author_email="winway1988@163.com",
    description=("Python project template"),
    license="BSD",
    keywords="example documentation tutorial",
    url="http://packages.python.org/an_example_pypi_project",
    long_description=read('README'),
    # packages=['foo', 'bar', 'bar.ba', 'tests'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    data_files=[('datafiles', ['./data/test.data'])],
    zip_safe=False,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "myfoo = foo.main:main",
        ],
    },
)
