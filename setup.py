# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:18:45 2022

@author: Juan Camilo González Vélez
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GD_Package",
    version="0.0.1",
    author="Juan_Camilo_Gonzalez",
    author_email="camilogv71@gmail.com",
    description="Gradient Descent Algorithm Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/camilogv71/GD_Package",
    project_urls={
        "Bug Tracker": "https://github.com/camilogv71/GD_Package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "GD_Package"},
    packages=["gdtest"],
    python_requires=">=3.8",
)
