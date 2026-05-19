class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "" :
            return True
        if len(s) > len(t):
            return False
        indexS = 0
        lenS = len(s)
        for i in t :
            if indexS == lenS : 
                return True
            if i == s[indexS]:
                indexS+=1
        return indexS == lenS





        # if the order wasnt matters
        # if s == "" :
        #     return True
        # s_set = set(s)
        # print(s_set)
        # print(t)
        # for i in t :
        #     print(i)
        #     if not s_set : 
        #         return True
        #     if i in s_set:
        #         print(s_set)
        #         s_set.remove(i)
        #         print(s_set)
        # return not s_set


def run_test(sol, s, t, expected, name):
    try:
        got = sol.isSubsequence(s, t)
        if got == expected:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   s        = {s!r}")
            print(f"   t        = {t!r}")
            print(f"   expected = {expected}")
            print(f"   got      = {got}")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement isSubsequence ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # official examples
        ("abc", "ahbgdc", True, "basic_true"),
        ("axc", "ahbgdc", False, "basic_false"),

        # empty cases
        ("", "abc", True, "empty_s"),
        ("abc", "", False, "empty_t"),
        ("", "", True, "both_empty"),

        # exact match
        ("abc", "abc", True, "exact_match"),

        # order matters
        ("ace", "abcde", True, "skip_chars"),
        ("aec", "abcde", False, "wrong_order"),

        # repeated characters
        ("aaa", "aaaaaa", True, "repeated_true"),
        ("aaaa", "aaa", False, "repeated_false"),

        # s longer than t
        ("abcdef", "abc", False, "s_longer_than_t"),

        # characters not present
        ("xyz", "abc", False, "not_present"),

        # complex
        ("abc", "aabbcc", True, "multiple_options"),
        ("abc", "acb", False, "relative_order_violation"),
    ]

    for s, t, expected, name in tests:
        run_test(sol, s, t, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
