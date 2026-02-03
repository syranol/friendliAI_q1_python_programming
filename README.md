# Common Lib 

Shared validation decorator for functions that accept `dict[str, int]` across
API services, data pipelines, CLI tools, and scheduled jobs.

## Files
- `common_lib.py` - shared decorator utility
- `tests/test_common_lib.py` - unit tests for validation behavior
- `demo.py` - simple demonstration of the decorator on two functions

## Setup (clone + venv)
```bash
git clone https://github.com/syranol/common-lib.git
cd common-lib
```

```bash
make venv
source .venv/bin/activate
```

## Run demo
```bash
make demo
```

Expected output (with the invalid case still commented):
```
Demo 1 — single positional argument
  sum_values({'apples': 2, 'oranges': 3}) -> 5

Demo 2 — multiple arguments incl. kwargs
  merge_counts({'apples': 2, 'oranges': 3}, b={'apples': 1}) -> {'apples': 3, 'oranges': 3}
```

If you uncomment the invalid example in `demo.py`, you'll see the decorator raise:
```
Traceback (most recent call last):
  File "demo.py", line 35, in main
    print(" sum_values({'apples': True}) ->", sum_values(bad))
  File "common_lib.py", line 47, in wrapper
    _validate_dict_str_int(arg, where=f"argument at position {index}")
  File "common_lib.py", line 30, in _validate_dict_str_int
    raise TypeError(
TypeError: argument at position 0 key 'apples' has non-int value True (type bool)
```

## Run tests (make)
```bash
make test
```


## Requirements
- Python 3.11 available as `python3.11`

## Notes / assumptions
- "Whole number" is treated as `int` but not `bool` (since `bool` is a subclass of `int`).
- The decorator validates all positional and keyword arguments are `dict[str, int]`.
  If you only want to validate a subset of parameters, the decorator can be adapted.
- `ParamSpec` and `TypeVar` preserve the wrapped function's full signature and return type
  for type checkers, so the decorator doesn't erase parameter/return typing.

## AI Assistance
This project was developed with the assistance of an AI coding tool used as a design and review aid, not as an autonomous code generator. I used AI intentionally to research tradeoffs, validate assumptions, and close knowledge gaps while retaining full ownership of the design and implementation. Specifically, I used AI to:

- Validate decorator structure and modern typing patterns (e.g., ParamSpec, TypeVar) against Python 3.11 best practices
- Evaluate whether a decorator was the appropriate shared utility by comparing alternatives such as inline validation, custom wrapper types, and schema-based approaches (e.g., pydantic-style models)
- Identify edge cases and subtle language behaviors (such as bool being a subclass of int) to ensure correct and defensive validation logic
- Refine error messages, docstrings, and API ergonomics to improve developer experience and failure clarity
- Review workflow scaffolding (Makefile, virtualenv setup, and test commands) to ensure reproducibility and ease of use

Throughout the process, AI was used to surface potential blind spots and prompt deeper investigation, allowing me to fully understand and justify each design choice. All architectural decisions, implementation details, and final edits were made, reviewed, and integrated by me.
