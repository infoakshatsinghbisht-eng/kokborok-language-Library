# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.md")
long_description = open(readme_path, encoding="utf-8").read() if os.path.exists(readme_path) else ""

setup(
    name="kokborok-language-library",
    version="1.0.0",
    author="Akshat Singh Bisht",
    author_email="infoakshatsinghbisht@gmail.com",
    maintainer="Akshat Singh Bisht",
    maintainer_email="infoakshatsinghbisht@gmail.com",
    description="Kokborok (Kókborok) Language Library: 100,000+ Headwords, 300,000+ Inflections, Multi-dialect Translation, NLP Toolkit, and Tripura Cultural Heritage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/infoakshatsinghbisht-eng/kokborok-language-Library",
    project_urls={
        "Homepage": "https://akshatsinghbisht.com/",
        "GitHub": "https://github.com/infoakshatsinghbisht-eng/kokborok-language-Library",
        "LinkedIn": "https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/",
        "Amazon Author": "https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28",
        "ResearchGate": "https://www.researchgate.net/profile/Akshat-Bisht-8",
        "Bug Tracker": "https://github.com/infoakshatsinghbisht-eng/kokborok-language-Library/issues",
    },
    packages=find_packages(exclude=["tests*", "examples*"]),
    include_package_data=True,
    package_data={
        "kokborok.lexicon": ["data/*.json"],
        "kokborok.culture": ["data/*.json"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "kokborok=kokborok.cli:main",
        ],
    },
)
