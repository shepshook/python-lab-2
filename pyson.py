import textwrap
from os import linesep as ls


def serialize(obj):
    if isinstance(obj, dict):
        result = f"{{{ls}"
        items = []
        for k, v in obj.items():
            items.append(f"\"{k}\": {serialize(v)}")
        result += textwrap.indent(f",{ls}".join(items), "  ")
        result += f"{ls}}}"
        return result

    elif isinstance(obj, list) or isinstance(obj, tuple):
        result = f"[{ls}"
        items = []
        for item in obj:
            items.append(f"{serialize(item)}")
        result += textwrap.indent(f",{ls}".join(items), "  ")
        result += f"{ls}]"
        return result

    elif isinstance(obj, str):
        return f"\"{obj}\""

    elif isinstance(obj, int) or isinstance(obj, float):
        return str(obj)

    elif isinstance(obj, bool):
        return "true" if obj else "false"

    elif obj is None:
        return "null"

    else:
        try:
            props = getattr(obj, "__dict__")
            return serialize(props)
        except AttributeError:
            raise ValueError("Object has no __dict__ attribute")


class NestedClass:
    def __init__(self):
        self.tup = (1, (2, 3))


class TestClass:
    def __init__(self):
        self.s = "zen of python"
        self.l = [1, 2, 5]
        self.n = 123
        self.t = (3, 4, 5)
        self.d = {"a": 1, "b": 4}
        self.b = False
        self.c = NestedClass()
