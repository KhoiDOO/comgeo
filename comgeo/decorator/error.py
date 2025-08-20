import functools

def not_self_implemented(func):
    """Decorator to raise NotImplementedError for methods that are not implemented."""
    def wrapper(self, *args, **kwargs):
        raise NotImplementedError(f"{func.__name__} is not implemented for {self.__class__.__name__}.")
    return wrapper

def self_implemented(func):
    """Decorator to check if the method is implemented."""
    def wrapper(self, *args, **kwargs):
        return func(self, *args, **kwargs)
    return wrapper

def not_self_instance(func):
    """Decorator to check if the argument is an instance of a specific class."""
    def wrapper(self, *args, **kwargs):
        # Only check if there are positional arguments
        if args and not isinstance(args[0], self.__class__):
            raise TypeError(f"{func.__name__} is only supported for {self.__class__.__name__} instances.")
        return func(self, *args, **kwargs)
    return wrapper

def not_instance(cls):
    """Decorator to check if the argument is an instance of a specific class."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if args and not isinstance(args[0], cls):
                raise TypeError(f"{func.__name__} is only supported for {cls.__name__} instances.")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator