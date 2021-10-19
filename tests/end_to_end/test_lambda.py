import pytest

TESTS_CASES = [
    (
        [
            """a = 10
b = lambda x: x + 10
c = b(a)
"""
        ],
        [("value", "c", 20)],
    ),
    (
        [
            """list_1 = [1,2,3,4,5,6,7,8,9]
list_2 = list(filter(lambda x: x%2==0, list_1))
"""
        ],
        [("valuearray", "list_2", [2, 4, 6, 8])],
    ),
    (
        [
            """list_1 = [1,2,3,4,5,6,7,8,9]
cubed = map(lambda x: pow(x,3), list_1)
final_value = list(cubed)"""
        ],
        ["valuearray", "final_value", [1, 8, 27, 64, 125, 216, 343, 512, 729]],
    ),
    (
        [
            """a = 10
b = lambda x: x + a
c = b(10)
"""
        ],
        [
            ("value", "c", 20),
            (
                "artifact",
                "c",
                """a = 10
b = lambda x: x + a
c = b(10)""",
            ),
        ],
    ),
]


@pytest.mark.xfail
@pytest.mark.parametrize("code, asserts", TESTS_CASES)
def test_import(execute, assertionist, code, asserts):
    res = execute(code[0])
    assertionist(res, asserts)
