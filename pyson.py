import textwrap

def serialize(obj):
    if isinstance(obj, dict):
        result = "{\n"
        items = ""
        for i, (k, v) in enumerate(obj.items()):
            items += f"\"{k}\": {serialize(v)}"
            if i < len(obj.items()) - 1:
                items += ","
            items += "\n"
        items = textwrap.indent(items, "  ")
        result += items
        result += "}"
        return result

    elif isinstance(obj, list) or isinstance(obj, tuple):
        result = "[\n"
        items = ""
        for i, item in enumerate(obj):
            items += f"{serialize(item)}"
            if i < len(obj) - 1:
                items += ","
            items += "\n"
        items = textwrap.indent(items, "  ")
        result += items
        result += "]"
        return result

    elif isinstance(obj, str):
        return f"\"{obj}\""

    elif isinstance(obj, int):
        return obj

    elif isinstance(obj, bool):
        return "true" if obj else "false"

    elif obj is None:
        return "null"

    elif isinstance(obj, object):
        return serialize(obj.__dict__)


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


#print(serialize(TestClass()))
