from typing import List
from collections import Counter


# Group Anagrams - test harness
# You asked: don't fill Solution, only main + test cases.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAnag = {}
        for i in strs:
            if not dictAnag:
                sortedStr = "".join(sorted(i))
                dictAnag[sortedStr] = [i]
            else:
                sortedStr = "".join(sorted(i))
                if sortedStr in dictAnag :
                    dictAnag[sortedStr].append(i)
                else:
                    dictAnag[sortedStr] = [i]
        lst = list(dictAnag.values())
        return lst



def normalize(groups: List[List[str]]) -> List[List[str]]:
    """Sort items within each group, then sort groups for order-insensitive compare."""
    cleaned = []
    for g in groups:
        assert isinstance(g, list), f"Each group must be a list, got {type(g)}"
        for w in g:
            assert isinstance(w, str), f"Each item must be str, got {type(w)}"
        cleaned.append(sorted(g))
    cleaned.sort()
    return cleaned


def run_test(name: str, strs: List[str], expected: List[List[str]]):
    sol = Solution()
    out = sol.groupAnagrams(strs)

    assert isinstance(out, list), f"{name}: Expected list of lists, got {type(out)}"
    # Basic structural validation:
    for g in out:
        assert isinstance(g, list), f"{name}: Each group must be a list, got {type(g)}"

    # Compare normalized forms (ignore order of groups and order within group)
    assert normalize(out) == normalize(expected), (
        f"{name}: Grouping mismatch.\n"
        f"Input: {strs}\n"
        f"Expected(normalized): {normalize(expected)}\n"
        f"Got(normalized): {normalize(out)}"
    )
    print(f"✅ {name} passed -> {out}")


def main():
    tests = [
        (
            "basic_example",
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (
            "single_word",
            ["abc"],
            [["abc"]],
        ),
        (
            "empty_string_only",
            [""],
            [[""]],
        ),
        (
            "empty_with_others",
            ["", "", "a", "b", "ab", "ba"],
            [["", ""], ["a"], ["b"], ["ab", "ba"]],
        ),
        (
            "duplicates_words",
            ["aa", "aa", "bb", "bb", "ab", "ba", "ab"],
            [["aa", "aa"], ["bb", "bb"], ["ab", "ba", "ab"]],
        ),
        (
            "all_unique_no_anagrams",
            ["abcd", "efgh", "ijkl"],
            [["abcd"], ["efgh"], ["ijkl"]],
        ),
        (
            "multi_group_same_size",
            ["listen", "silent", "enlist", "google", "gogole"],
            [["listen", "silent", "enlist"], ["google", "gogole"]],
        ),
        (
            "many_small",
            ["a", "a", "a", "b", "b", "c"],
            [["a", "a", "a"], ["b", "b"], ["c"]],
        ),
    ]

    for name, strs, expected in tests:
        run_test(name, strs, expected)

    print("\n🎉 All test cases passed.")


if __name__ == "__main__":
    main()
