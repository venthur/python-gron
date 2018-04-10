import json
from typing import Any


def walk(node: Any, name: str) -> str:
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
    if ('-' in name or ' ' in name):
        return '["{}"]'.format(name[1:])
    return name


def gron(input_: str) -> str:
    python = json.loads(input_)
    output = walk(python, 'json')
    return output
