from setuptools import setup, find_packages

setup(
    name="computational-geometry",
    version="0.0.2",
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