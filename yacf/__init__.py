"""

[//] # "docstring is used to autogenerate the README.md file."

# YACF - Yet Another Configuration Framework

Simple framework to parse multiple configuration files of different formats
and update them.


## Usage

The usage of this framework is straight-forward.

Create a Configuration instance. When creating one, give the inputs to read
from as arguments. The input can be either a dictionary, to be immediately 
used, or alternatively a file name which ends on one of the supported file
types below.

Afterwards, call the `load` function on the configuration instance. This
function allows to define additional inputs. It's a matter of choice whether
one wants to define the inputs in the constructor or in the `load` call.

The `load` function uses the previously defined configuration inputs. The 
function builds one large configuration dictionary out of all the inputs.
Overlapping parameters are always overwritten.

This makes it easy to define configurations of different priorities. One good
approach is to define the configuration inputs as follows:

```
[defaults, custom configuration, environment variables, command line arguments]
```

To access the values of the configuration, one can either use the regular
access of dictionaries, e.g. a concatenation of gets(). Alternatively one can
simply use dot notation:

```
config = Configuration('api-config.json').load()
sample = config.get('api').get('hostname')

# Alternative dot notation
sample = config.get('api.hostname')
```


## Additional Features

### Custom Seperator

If you, for some reason dislike the regular seperator '.' in the dot notation
you can choose a custom one when initializing the configuration instance.



## Supported File Types

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
