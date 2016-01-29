Timer
=====

A helpful little timer that can tell you how long it takes a piece of code to execute.

Usage
=====

Installation
------------

Run `setup.py`.

Basic Usage
-----------

Once installed, the timer can be used like this:

```python
from timer import timer

with timer():
    expensive_operation()
```

When `expensive_operation` finishes executing, the elapsed time will be displayed:

```
Elapsed time: 0:00:01.455517
```

Additional Options
------------------

You can also specify a custom label and display function:

```python
with timer(label='Operation 1', display=logger.debug):
    operation_1()
```

When `operation_1` finishes executing, the elapsed time will be displayed:

```
DEBUG:Operation 1: 0:00:00.013547
```

Bugs and Feature Requests
=========================

Feature Requests
----------------

None

Known Bugs
----------

None

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

Remember: [GitHub is not my CV.](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/)
