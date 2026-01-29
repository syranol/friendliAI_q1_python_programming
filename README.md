# Q1 - dict[str, int] decorator

## Files
- `common_lib.py` - shared decorator utility intended for reuse across API services,
  data processing pipelines, CLI tools, and scheduled billing jobs; includes a small example

## Run (make)
```bash
cd friendliAI_q1_python_programming
make run
```

## Requirements
- Python 3.11 available as `python3.11`

## Notes / assumptions
- "Whole number" is treated as `int` but not `bool` (since `bool` is a subclass of `int`).
- The decorator validates all positional and keyword arguments are `dict[str, int]`.
  If you only want to validate a subset of parameters, the decorator can be adapted.
- `ParamSpec` and `TypeVar` preserve the wrapped function's full signature and return type
  for type checkers, so the decorator doesn't erase parameter/return typing.
# friendliAI_q1_python_programming
