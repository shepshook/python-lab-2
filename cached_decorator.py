def cached(func):
    cache = {}

    def wrapper(*args, **kwargs):
        nonkeyed_args = tuple(args)
        keyed_args = tuple(sorted(kwargs.items()))
        key = hash((nonkeyed_args, keyed_args))
        if key in cache.keys():
            return cache[key]
        result = func(*args, **kwargs)
        if result:
            cache[key] = result
        return result

    return wrapper
