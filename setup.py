from setuptools import setup

description = \
    """
    This module is a client for PERMAFROST
    """

setup(
    name = 'pfS3',
    version = '0.0.1',
    url = "https://github.com/ruebot/pfS3",
    author = "Nick Ruest",
    author_email = "ruestn@gmail.com",
    py_modules = ['pfS3'],
    scripts = ['pfS3'],
    description = description,
    platforms = ['POSIX'],
    test_suite = 'test',
    classifiers = [
      'License :: GPLv3',
      'Intended Audience :: Developers',
      'Topic :: Communications :: File Sharing',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: System :: Filesystems',
    ],
)
