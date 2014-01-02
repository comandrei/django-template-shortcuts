import os.path
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name="django-template-shortcuts",
    version="0.1",
    packages=find_packages(),
    author="Andrei Coman",
    author_email="comandrei@gmail.com",
    install_requires=["django>=1.3"],
    url="https://github.com/comandrei/django-template-shortcuts/",
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    long_description=README
)
