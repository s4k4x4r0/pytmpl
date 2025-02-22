"""
Main CLI entrypoint.

Copyright 2025 Vlad Emelianov
"""

import sys


def print_info() -> None:
    """
    Print package info to stdout.
    """
    sys.stdout.write(
        "Type annotations for boto3 STS 1.36.26\n"
        "Version:         1.36.26\n"
        "Builder version: 8.9.2\n"
        "Docs:            https://youtype.github.io/types_boto3_docs/types_boto3_sts//\n"
        "Boto3 docs:      https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#sts\n"
        "Other services:  https://pypi.org/project/boto3-stubs/\n"
        "Changelog:       https://github.com/youtype/mypy_boto3_builder/releases\n"
    )


def print_version() -> None:
    """
    Print package version to stdout.
    """
    sys.stdout.write("1.36.26\n")


def main() -> None:
    """
    Main CLI entrypoint.
    """
    if "--version" in sys.argv:
        print_version()
        return
    print_info()


if __name__ == "__main__":
    main()
