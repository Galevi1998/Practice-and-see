class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenNeedle = len(needle)
        lenHaystack = len(haystack)
        if lenNeedle > lenHaystack:
            return -1
        elif lenNeedle == lenHaystack:
            return 0 if needle == haystack else -1
        elif lenNeedle == 0 :
            return 0
        for i in range(len(haystack)):
            if i+lenNeedle <= lenHaystack and haystack[i:i+lenNeedle] == needle :
                print(haystack[i:i+lenNeedle] , needle)
                return i
            elif i+lenNeedle > lenHaystack : 
                return -1
        return -1


def run_test(haystack, needle, expected, test_name):
    sol = Solution()
    result = sol.strStr(haystack, needle)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   haystack:", repr(haystack))
        print("   needle  :", repr(needle))
        print("   expected:", expected)
        print("   got     :", result)


def main():
    tests = [

        # 🔹 Basic match
        ("sadbutsad", "sad", 0, "basic_match_start"),

        # 🔹 Match in middle
        ("leetcode", "code", 4, "match_middle"),

        # 🔹 No match
        ("leetcode", "leeto", -1, "no_match"),

        # 🔹 Full string match
        ("abc", "abc", 0, "full_match"),

        # 🔹 Needle longer than haystack
        ("abc", "abcd", -1, "needle_longer"),

        # 🔹 Repeated pattern
        ("aaaaa", "aaa", 0, "repeated_pattern"),

        # 🔹 Overlapping possibility
        ("mississippi", "issipi", 1, "overlapping_match"),

        # 🔹 Single character match
        ("a", "a", 0, "single_char_match"),

        # 🔹 Single character no match
        ("a", "b", -1, "single_char_no_match"),

        # 🔹 Empty needle (LeetCode guarantees needle length >= 1, but good for local)
        ("abc", "", 0, "empty_needle"),

        # 🔹 Both empty
        ("", "", 0, "both_empty"),

        # 🔹 Needle at end
        ("hello", "lo", 3, "match_end"),

        # 🔹 Multiple occurrences, must return first
        ("abcabcabc", "cab", 2, "first_occurrence"),

        # 🔹 Very long haystack
        ("a"*1000 + "b", "ab", 999, "long_haystack"),

    ]

    for haystack, needle, expected, name in tests:
        run_test(haystack, needle, expected, name)


if __name__ == "__main__":
    main()
