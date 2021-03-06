import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyleecan",
    version="0.0.0",
    author="Pyleecan Developers",
    author_email="",
    description="Python Library for Electrical Engineering Computational Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eomys/pyleecan",
    download_url="https://github.com/Eomys/pyleecan.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    install_requires=[
        "cloudpickle==1.3.0",
        "ddt==1.3.1",
        "gmsh-sdk==4.5.5.post1",
        "matplotlib==3.2.1",
        "mock==4.0.2",
        "numpy==1.18.2",
        "pandas==1.0.3",
        "pyfemm==0.1.0",
        "PyQt5==5.14.1",
        "PyQt5-sip==12.7.1",
        "pytest==5.4.1",
        "scipy==1.4.1",
        "xlrd==1.2.0",
        "deap==1.3.1",
        "SciDataTool>=0.0.4",
    ],
)
