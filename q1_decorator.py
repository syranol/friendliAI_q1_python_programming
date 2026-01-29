from __future__ import annotations

from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def _validate_dict_str_int(value: object, *, where: str) -> None:
    if not isinstance(value, dict):
        raise TypeError(
            f"{where} must be dict[str, int]; got {type(value).__name__}"
        )

    for key, item in value.items():
        if not isinstance(key, str):
            raise TypeError(
                f"{where} has non-str key {key!r} (type {type(key).__name__})"
            )
        # bool is a subclass of int; treat it as invalid for "whole number".
        if isinstance(item, bool) or not isinstance(item, int):
            raise TypeError(
                f"{where} key {key!r} has non-int value {item!r} "
                f"(type {type(item).__name__})"
            )


def enforce_dict_str_int(func: Callable[P, R]) -> Callable[P, R]:
    """ Decorator for ensure all positional/keyword args are dict[str, int] before calling func."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        """ Returned function that wraps the original function. """
        for index, arg in enumerate(args):
            _validate_dict_str_int(arg, where=f"argument at position {index}")
        for name, arg in kwargs.items():
            _validate_dict_str_int(arg, where=f"argument '{name}'")
        return func(*args, **kwargs)

    return wrapper


@enforce_dict_str_int
def sum_values(data: dict[str, int]) -> int:
    return sum(data.values())


if __name__ == "__main__":
    print(sum_values({"apples": 0, "bananas": 1}))
    # Uncomment to see the validation error:
    # print(sum_values({"bad": True}))
