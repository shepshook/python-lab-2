def cached(cache: dict):
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonkeyed_args = tuple(repr(args))
            keyed_args = (tuple(repr(kwargs.keys())), tuple(repr(kwargs.items())))
            key = hash((nonkeyed_args, keyed_args))
            if key in cache.keys():
                return cache[key]
            result = func(*args, **kwargs)
            if result:
                cache[key] = result
            return result

        return wrapper

    return decorator
