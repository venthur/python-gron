import json
from typing import Any


def walk(node: Any, name: str) -> str:
    """Translate Python element to JSON.

    This method recursively visits each element of a Python object and
    returns the JSON representation.

    Parameters
    ----------
    node :
        A python object (e.g. dict, list, int, etc)
    name : str
        The name (i.e. path) of the parent element

    Returns
    -------
    str:
        Transformed JSON for this element

    """
    if node is None:
        return "{name} = {value};".format(name=name, value='null')
    elif isinstance(node, bool):
        return "{name} = {value};".format(name=name, value=str(node).lower())
    elif isinstance(node, (str, bytes)):
        return '{name} = "{value}";'.format(name=name, value=node)
    elif isinstance(node, dict):
        res = []
        res.append("{name} = {{}};".format(name=name))
        for k, v in sorted(node.items()):
            res.append(walk(v, name + convert('.' + k)))
        return '\n'.join(sorted(res))
    elif isinstance(node, (list, tuple)):
        res = []
        res.append("{name} = [];".format(name=name))
        for i, e in enumerate(node):
            res.append(walk(e, name + convert(str([i]))))
        return '\n'.join(res)

    else:
        return "{name} = {value!r};".format(name=name, value=node)


def convert(name: str) -> str:
    """Convert path name into valid JSON.

    Parameters
    ----------
    name : str
        a path name

    Output
    ------
    str
        valid JSON path

    """
    if ('-' in name or ' ' in name):
        return '["{}"]'.format(name[1:])
    return name


def gron(input_: str) -> str:
    """Transform JSON into parseable str.

    This method takes a JSON string and transforms it into a grepable
    equivalent form.

    Parameters
    ----------
    input_ : str
        JSON

    Output
    ------
    str
        Transformed output

    """
    python = json.loads(input_)
    output = walk(python, 'json')
    return output
