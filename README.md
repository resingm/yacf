

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



## Caveats

The framework is solely implemented and tested on Linux. I can not guarantee
for any expected behaviour on other platforms. 
If you use the framework on another platform, please share your experiences
with me.





# License

MIT License Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next
paragraph) shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
