"""
TODO: Add docstring
"""

from typing import Any, Union

# third party

# first party


def deep_update(this: dict, other: dict) -> dict:
    """Recursively updates the values of a dictionary.
    Just as with the regular dict.update() implementation does the function
    preferably uses the values of the other dictionary.

    Raises a type error, if not both of the parameters are dictionaries.

    :param value: Dictionary to update
    :param other: Other dictionary to merge into the first one.
    :return: Updated dictionary
    """

    for k, v in other.items():
        if isinstance(v, dict):
            this[k] = deep_update(this.get(k, {}), v)
        else:
            this[k] = other[k]

    return this


def add_dot_notations(d: dict, seperator: str, prefix: str = None) -> dict:
    """Takes a dictionary as input and concatenates the different keys together
    to access each configuration parameter with a single key.

    :param conf: configuration where the dot notation should be added.
    :param seperator: Seperating character to use for the dot-notation.
    """
    keys = d.keys()
    for k in keys:
        key = k if prefix is None else f"{prefix}.{k}"

        if isinstance(d[k], dict):
            v = add_dot_notations(d[k], seperator, prefix=key)
            d[k] = v

        d.update({key: v})

    return d
