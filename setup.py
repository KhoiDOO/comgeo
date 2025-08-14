from setuptools import setup, find_packages

import os

def get_version():
    pyproject_file = "pyproject.toml"
    with open(pyproject_file, "r") as f:
        txt = f.read()
    for line in txt.splitlines():
        if line.startswith("version"):
            return line.split("=")[1].strip().strip('"')

def get_name():
    pyproject_file = "pyproject.toml"
    with open(pyproject_file, "r") as f:
        txt = f.read()
    for line in txt.splitlines():
        if line.startswith("name"):
            return line.split("=")[1].strip().strip('"')

setup(
    name=get_name(),
    version=get_version(),
    description="Computational Geometry",
    author="KhoiDOO",
    author_email="khoido8899@gmail.com",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)