#!/usr/bin/env python

from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name="blueshell",
      version="0.0.1",
      description="Blue Shell is a chat shell for local ai service endpoint",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="marsliu",
      author_email="mars.liu@outlook.com",
      url="https://github.com/MarchLiu/blue-shell",
      license="MIT",
      packages=["blueshell", "test"],
      package_dir={
          "blueshell": "src/blueshell",
          "test": "src/test"
      },
      install_requires=[
          "prompt_toolkit",
          "requests"
      ],
      classifiers=[
          "Topic :: Utilities",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3 :: Only",
          "License :: OSI Approved :: MIT License"
      ]
      )
