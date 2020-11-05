"""

[//] # "docstring is used to autogenerate the README.md file."

# YACF - Yet Another Configuration Framework

Simple framework to parse multiple configuration files of different formats
and update them.


## Usage

[//] # "TODO: usage"


## Features

Supported file types:

* ini
* json
* toml

"""


# first party
from .configuration import Configuration

__version__ = (0, 1, 0)


def version() -> str:
    """Returns the version as a formatted string
    :return: Version string
    """
    return ".".join(__version__)
