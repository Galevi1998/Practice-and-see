
# Valid Anagram - test harness
# You asked: don't fill Solution, only main + test cases.
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        return Counter(s) == Counter(t)
        # dict = {}
        # for i in s:
        #     dict[i] = dict.get(i, 0) + 1
        # for i in t :
        #     dict[i] = dict.get(i, 0) - 1
        #     if dict[i] == 0 :
        #         del dict[i]
        # if not dict:
        #     return True
        # return False


def run_test(name: str, s: str, t: str, expected: bool):
    sol = Solution()
    out = sol.isAnagram(s, t)
    assert isinstance(out, bool), f"{name}: Expected bool, got {type(out)}"
    assert out == expected, f"{name}: Expected {expected}, got {out}"
    print(f"✅ {name} passed -> {out}")


def main():
    tests = [
        ("basic_true", "anagram", "nagaram", True),
        ("basic_false", "rat", "car", False),
        ("different_lengths", "ab", "a", False),
        ("same_single_char", "a", "a", True),
        ("single_char_false", "a", "b", False),
        ("repeated_chars_true", "aacc", "ccaa", True),
        ("repeated_chars_false", "aacc", "ccac", False),
        ("empty_both", "", "", True),
        ("empty_one", "", "a", False),
        ("order_irrelevant", "listen", "silent", True),
        ("all_same_letters", "aaaaaa", "aaaaaa", True),
        ("close_but_not", "abcd", "abce", False),
        # Constraint-friendly stress-ish case (lowercase letters)
        ("long_repeats_true", "z" * 500 + "y" * 500, "y" * 500 + "z" * 500, True),
        ("long_repeats_false", "z" * 500 + "y" * 500, "y" * 499 + "z" * 501, False),
    ]

    for name, s, t, expected in tests:
        run_test(name, s, t, expected)

    print("\n🎉 All test cases passed.")


if __name__ == "__main__":
    main()
