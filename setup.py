from setuptools import setup, find_packages
setup(
    name = "django-template-shortcuts",
    version = "0.1",
    packages = find_packages(),
    author="Andrei Coman",
    author_email="comandrei@gmail.com",
    install_requires=["django>1.3"],
    test_requires=["nose"]

)
