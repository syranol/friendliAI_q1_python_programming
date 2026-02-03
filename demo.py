from __future__ import annotations

from common_lib import enforce_dict_str_int


@enforce_dict_str_int
def sum_values(data: dict[str, int]) -> int:
    return sum(data.values())


@enforce_dict_str_int
def merge_counts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    merged = a.copy()
    for k, v in b.items():
        merged[k] = merged.get(k, 0) + v
    return merged


def main() -> None:
    good = {"apples": 2, "oranges": 3}
    good2 = {"apples": 1}

    print("Goal: show the decorator allows only dict[str, int] inputs (positional and keyword).")

    print("\nDemo 1 — single positional argument")
    print("  sum_values({'apples': 2, 'oranges': 3}) ->", sum_values(good))

    print("\nDemo 2 — multiple arguments incl. kwargs")
    print("  merge_counts({'apples': 2, 'oranges': 3}, b={'apples': 1}) ->", merge_counts(good, b=good2))

    print("\nDemo 3 — invalid input (uncomment to see the raised ValueError)")

    # Uncomment to see validation error:
    # bad = {"apples": True}
    # print(" sum_values({'apples': True}) ->", sum_values(bad))


if __name__ == "__main__":
    main()
