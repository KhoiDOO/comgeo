def not_implemented(func):
    """Decorator to raise NotImplementedError for methods that are not implemented."""
    def wrapper(self, *args, **kwargs):
        raise NotImplementedError(f"{func.__name__} is not implemented for {self.__class__.__name__}.")
    return wrapper

def not_self_instance(func):
    """Decorator to check if the argument is an instance of a specific class."""
    def wrapper(self, other, *args, **kwargs):
        if not isinstance(other, self.__class__):
            raise NotImplementedError(f"{func.__name__} is only supported for {self.__class__.__name__} instances.")
        return func(self, other, *args, **kwargs)
    return wrapper