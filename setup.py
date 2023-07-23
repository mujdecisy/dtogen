import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="dtogen",
    version="0.0.7",
    description="DTO generator for Java, TypeScript, Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mujdecisy/dtogen",
    keywords=["python", "DTO", "generator"],
    author="mujdecisy",
    author_email="mujdecisy@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=['dtogen','dtogen.transformers','dtogen.filewriters'],
    include_package_data=True,
    install_requires=["mapperr", "pyyaml"],
)
