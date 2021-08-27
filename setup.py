import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

project_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(project_dir, "requirements.txt")) as f:
        reqd_pkgs = list(f.read().splitlines())

setuptools.setup(
    name="yt_aspect",
    version="0.0.1",
    author="Chris Havlin",
    author_email="chris.havlin@gmail.com",
    description="A yt plugin for loading ASPECT output",
    install_requires = reqd_pkgs,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrishavlin/yt_aspect",
    project_urls={
        "Bug Tracker": "https://github.com/chrishavlin/yt_aspect/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "yt_aspect"},
    packages=setuptools.find_packages(where="yt_aspect"),
    python_requires=">=3.6",
)
