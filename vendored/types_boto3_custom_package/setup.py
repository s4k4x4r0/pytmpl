"""
Setup script for types-boto3-custom.

Copyright 2025 Vlad Emelianov
"""

from pathlib import Path

from setuptools import setup  # type: ignore

LONG_DESCRIPTION = (Path(__file__).parent / "README.md").read_text()

setup(
    name="types-boto3-custom",
    version="1.36.26",
    packages=["boto3-stubs", "types_boto3_sts"],
    url="https://github.com/youtype/mypy_boto3_builder",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Custom type annotations for boto3 1.36.26 generated with mypy-boto3-builder 8.9.2",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Stubs Only",
    ],
    keywords="boto3 boto3-stubs type-annotations typeshed autocomplete",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={
        "boto3-stubs": ["py.typed", "*.pyi", "*/*.pyi"],
        "types_boto3_sts": ["py.typed", "*.pyi"],
    },
    python_requires=">=3.8",
    project_urls={
        "Documentation": "https://youtype.github.io/types_boto3_docs/",
        "Source": "https://github.com/youtype/mypy_boto3_builder",
        "Tracker": "https://github.com/youtype/mypy_boto3_builder/issues",
    },
    install_requires=[
        "botocore-stubs",
        "types-s3transfer",
        'typing-extensions; python_version<"3.12"',
    ],
    zip_safe=False,
)
