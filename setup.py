
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PROJET_PIP_TEST",
    version="0.0.1",
    author="Imen Ayari",
    author_email="ayari.imen@hotmail.com",
    description="This is a POC for creating a private pip ! ",
    long_description=long_description,
    url="https://github.com/ImenAyari/projet_pip_test.git",
    packages="PROJET_PIP_TEST",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)