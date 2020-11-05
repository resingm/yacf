# standard lib
from json import load as json_load
from os import path
from typing import Any

# third party
from toml import load as toml_load

# first party
from yacf.utils import deep_update, add_dot_notations

ACCEPTED_FILE_EXTENSIONS = {
    # TODO: Load ini file
    # ".ini":
    ".json": json_load,
    ".toml": toml_load,
}


class Configuration(object):
    """A Configuration object is the most important part of this entire framework.
    When creating one, one can add arbitrarily many input arguments. Furthermore,
    one can add additional configuration origins in the load function as well.

    The configuration instance will try to read from all the different inputs.
    It is important to know, that the order matters. The first arguments are the
    ones which have the least priority. As more inputs are added, as finer the
    configuration gets.

    It is recommended to first add all inputs to build one complete default set
    of configuration parameters. As soon as those are available, the customly
    configurable sources should be loaded, followed by possibly parsed environment
    variables and lastly, the dictionary of command line arguments should be
    added.

    This will end up in a complete stack of different configurations.

    To access configuration parameters, just call the `.get()` method. It mimics
    the dictionary `.get()` method, with an additional feature. You can also
    access configuration parameters by simply concatenating the keys in dot-notation.
    """

    def __init__(self, *args, seperator="."):
        """Creates a new configuration parser object. Use the *args parameter
        to parse an arbitrary number of different configuration resources,
        e.g. a default configuration file, a custom configuration file and
        some command line arguments.

        The seperator defines the type of character that is used for the key
        concatenation. By default, it is a '.', since it's called the
        'dot' notation.

        :param *args: Defines the configuration input
        :param seperator: Seperator character to use for the dot-notation
        """
        self._conf = {}
        self._seperator = seperator
        self._input = [arg for arg in args]

    def get(self, key: str, default=None) -> Any:
        """Tries to find the key in the dictionary and returns the value, if it exists.
        Function mimics the `dict.get()` function.

        :param key: The key to look for.
        :param default: The default value to return to.
        :return: value of the requested key.
        """
        # TODO: implement get

    def load(self, *args):
        """Loads the predefined input configuration files/dictionaries.
        Optionally, one can add even more input sources with this function.

        :param *args: files or dictionaries to add to configuration
        """
        self._input.join([arg for arg in args])

        for i in self._input:
            if isinstance(i, dict):
                # simply a dictionary
                other = i
            elif isinstance(i, str):
                # assume it is a path to a file
                try:
                    other = _readf(i)
                except Exception as e:
                    raise e
            else:
                raise TypeError(f"Cannot load a configuration of type {type(i)}")

            self._conf = deep_update(self._conf, other)

        self._conf = add_dot_notations(self._conf, self._seperator)


def _readf(file_path: str) -> dict:
    """Reads the content of a configuration file and parses it to a dictionary.
    Raises a FileNotFoundError if the file does not exist.

    :param file_path: path of the file to open
    """
    if not path.exists(file_path):
        raise FileNotFoundError(f"File cannot be found: '{file_path}'")

    # Checks which function should be used to load the file
    fn = [ext for ext in ACCEPTED_FILE_EXTENSIONS.keys() if file_path.endswith(ext)]

    if len(fn) < 1:
        raise NotImplementedError("File extension not supported.")

    with open(file_path, "r") as f:
        content = ACCEPTED_FILE_EXTENSIONS.get(fn[0]).__call__(f)
        assert isinstance(content, dict)
        return content
