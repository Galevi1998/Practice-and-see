from math import gcd


from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]



def run_test(sol: Solution, str1: str, str2: str, expected: str, name: str) -> None:
    try:
        got = sol.gcdOfStrings(str1, str2)
        if got == expected:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   str1     = {str1!r}")
            print(f"   str2     = {str2!r}")
            print(f"   expected = {expected!r}")
            print(f"   got      = {got!r}")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement gcdOfStrings ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # official-style basics
        ("ABCABC", "ABC", "ABC", "basic_1"),
        ("ABABAB", "ABAB", "AB", "basic_2"),
        ("LEET", "CODE", "", "no_common_divisor"),
        ("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "", "prefix_but_not_divisor"),


        # identical strings
        ("AAAA", "AAAA", "AAAA", "identical"),

        # one is repetition of the other
        ("XYZXYZXYZ", "XYZ", "XYZ", "str2_is_base"),
        ("TT", "T", "T", "single_char_base"),

        # gcd is empty because not compatible repetition
        ("ABAB", "ABBA", "", "same_length_but_not_repeatable"),
        ("ABCABC", "ABCA", "", "prefix_but_not_divisor"),

        # edge-ish
        ("A", "A", "A", "one_char_equal"),
        ("A", "B", "", "one_char_different"),
        ("AAAAAA", "AAA", "AAA", "multiple_As"),
        ("AAAAAA", "AA", "AA", "gcd_is_AA"),
    ]

    for s1, s2, expected, name in tests:
        run_test(sol, s1, s2, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
