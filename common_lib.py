"""Shared decorator for dict[str, int] validation.

Intended consumers include API services, data processing pipelines, CLI tools,
and scheduled billing jobs within a large monorepo.
"""

from __future__ import annotations

from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def _validate_dict_str_int(value: object, *, where: str) -> None:
    """Validate that value is dict[str, int], raising TypeError with context."""
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
    """Decorator enforcing dict[str, int] for all args before calling func.

    Raises:
        TypeError: If any positional or keyword argument is not dict[str, int].
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        """Return function that wraps the original function."""
        for index, arg in enumerate(args):
            _validate_dict_str_int(arg, where=f"argument at position {index}")
        for name, arg in kwargs.items():
            _validate_dict_str_int(arg, where=f"argument '{name}'")
        return func(*args, **kwargs)

    return wrapper
