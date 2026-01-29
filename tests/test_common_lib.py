import unittest

from common_lib import enforce_dict_str_int


@enforce_dict_str_int
def echo(data: dict[str, int]) -> dict[str, int]:
    return data


@enforce_dict_str_int
def sum_two(a: dict[str, int], *, b: dict[str, int]) -> int:
    return sum(a.values()) + sum(b.values())


class TestEnforceDictStrInt(unittest.TestCase):
    def test_valid_dict(self) -> None:
        self.assertEqual(echo({"a": 1, "b": 2}), {"a": 1, "b": 2})

    def test_rejects_non_dict(self) -> None:
        with self.assertRaises(TypeError):
            echo([("a", 1)])  # type: ignore[arg-type]

    def test_rejects_non_str_key(self) -> None:
        with self.assertRaises(TypeError):
            echo({1: 2})  # type: ignore[dict-item]

    def test_rejects_bool_value(self) -> None:
        with self.assertRaises(TypeError):
            echo({"a": True})  # type: ignore[dict-item]

    def test_rejects_non_int_value(self) -> None:
        with self.assertRaises(TypeError):
            echo({"a": 1.2})  # type: ignore[dict-item]

    def test_valid_positional_and_keyword(self) -> None:
        self.assertEqual(sum_two({"a": 1}, b={"b": 2}), 3)

    def test_rejects_keyword(self) -> None:
        with self.assertRaises(TypeError):
            sum_two({"a": 1}, b={"b": "x"})  # type: ignore[dict-item]


if __name__ == "__main__":
    unittest.main()
