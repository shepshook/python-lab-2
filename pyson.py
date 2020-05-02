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

    elif isinstance(obj, list):
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

class B:
    def __init__(self):
        self.s = "string of B"
        self.d = {"a": 1, "b": 2, "c": 3}

class A:
    def __init__(self):
        self.a = 1
        self.b = [1, 2, 3]
        self.c = B()

#serialize({"a": 1, "b": 2, "c": 3})

#serialize([1, 1, 2, 3, 5, 8, 13])

#print(A().__dict__)

print(serialize(A()))