from typing import Any

def check_type(var: Any, expected_type: type, var_name: str):
    if not isinstance(var, expected_type):
        raise TypeError(f"Expected {expected_type} for {var_name}, got {type(var)}")

def check_consistency(args: list[Any], var_name: str):
    if not all(isinstance(arg, type(args[0])) for arg in args):
        raise TypeError(f"All arguments must be of the same type for {var_name}")