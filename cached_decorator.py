def cached(func):
    cache = {}

    def wrapper(*args, **kwargs):
        nonkeyed_args = tuple(args)
        keyed_args = tuple(sorted(kwargs.items()))
        key = (nonkeyed_args, keyed_args)
        result = cache.get(key)
        if result:
            return result
        result = func(*args, **kwargs)
        if result:
            cache[key] = result
        return result

    return wrapper
