""" Gron's core functions  """

import json
from typing import Any, FrozenSet, Iterable, Optional


RESERVED_WORDS = frozenset("""
break case catch class const continue debugger default delete do else export
extends false finally for function if import in instanceof new null return
super switch this throw true try typeof var void while with yield
""".strip().split())


class Gron:

    root_name: str = 'json'
    quote_names: bool = True
    reserved_words: FrozenSet[str] = RESERVED_WORDS
    line_format: str = '{name} = {value};'
    initialize_structures: bool = True
    sort_keys: bool = True

    def default(self, value: any) -> str:
        return '{!r}'.format(value)

    def decode_bytes(self, value: bytes) -> str:
        return value.decode('utf-8', errors='replace')

    def force_quote_name(self, name: str) -> str:
        return json.dumps([name])

    def verbose_quote_name(self, name: Any) -> str:
        """ Convert path name (e.g. a dict key) into valid JSON identifier. """
        if not isinstance(name, str):
            name = str(name)
        if not self.quote_names:
            return False, name
        if '-' in name or ' ' in name:
            return True, self.force_quote_name(name)
        if name in self.reserved_words:
            return True, self.force_quote_name(name)
        return False, name

    def quote_name(self, name: Any, dot_unquoted: bool = False) -> str:
        """ Convert path name (e.g. a dict key) into valid JSON identifier. """
        quoted, result = self.verbose_quote_name(name)
        if dot_unquoted and not quoted:
            result = '.{}'.format(result)
        return result

    def dump_none(self, node: None, name: str) -> Iterable[str]:
        yield self.line_format.format(name=name, value='null')

    def dump_bool(self, node: bool, name: str) -> Iterable[str]:
        value = 'true' if node else 'false'
        yield self.line_format.format(name=name, value=value)

    def dump_str(self, node: str, name: str) -> Iterable[str]:
        value = json.dumps(node)
        yield self.line_format.format(name=name, value=value)

    def dump_bytes(self, node: bytes, name: str) -> Iterable[str]:
        value = self.decode_bytes(node)
        return self.dump_str(value, name)

    def dump_dict(self, node: dict, name: str) -> Iterable[str]:
        if self.initialize_structures:
            yield self.line_format.format(name=name, value='{}')

        items = node.items()
        if self.sort_keys:
            items = sorted(items)

        children_lst = [
            self.walk(
                value,
                name='{}{}'.format(
                    name,
                    self.quote_name(key, dot_unquoted=True),
                ),
            )
            for key, value in items
        ]
        if self.sort_keys:
            children_lst = [list(children) for children in children_lst]
            children_lst.sort()

        for children in children_lst:
            for child in children:
                yield child

    def dump_list(self, node: bool, name: str) -> Iterable[str]:
        if self.initialize_structures:
            yield self.line_format.format(name=name, value='[]')
        for idx, value in enumerate(node):
            children = self.walk(value, name='{}[{}]'.format(name, idx))
            for child in children:
                yield child

    def dump_any(self, node: Any, name: str) -> Iterable[str]:
        value = self.default(node)
        yield self.line_format.format(name=name, value=value)

    def walk(self, node: Any, name: Optional[str] = None) -> Iterable[str]:
        """
        Translate Python element to JSON.

        This method recursively visits each element of a Python object and
        returns the JSON representation.

        Parameters
        ----------
        node
            A python object (e.g. dict, list, int, etc)
        name : str
            The name (i.e. path) of the parent element

        Returns
        -------
        str
            Transformed JSON for this element
        """
        if name is None:
            name = self.quote_name(self.root_name)

        if node is None:
            handler = self.dump_none
        elif isinstance(node, bool):
            handler = self.dump_bool
        elif isinstance(node, str):
            handler = self.dump_str
        elif isinstance(node, bytes):
            handler = self.dump_bytes
        elif isinstance(node, dict):
            handler = self.dump_dict
        elif isinstance(node, (list, tuple)):
            handler = self.dump_list
        else:
            handler = self.dump_any
        for item in handler(node, name):
            yield item

    def gron(self, input_: Any) -> Iterable[str]:
        """Transform JSON into parseable str.

        This method takes a JSON string and transforms it into a grepable
        equivalent form.

        Parameters
        ----------
        input_ : str
            JSON

        Returns
        -------
        str
            Transformed output

        """
        if isinstance(input_, (bytes, str)):
            data = json.loads(input_)
        else:
            data = input_
        return self.walk(data)

    def __call__(self, input_: Any) -> str:
        return self.gron(input_)


def gron(input_: Any) -> str:
    return '\n'.join(Gron().gron(input_))
