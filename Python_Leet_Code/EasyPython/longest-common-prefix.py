from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lenStrs = len(strs)
        if lenStrs == 1 : 
            return strs[0]
        if lenStrs == 0 : 
            return ""
        helper = strs[0]
        for i in strs : 
            while i.startswith(helper) == False and helper != "":
                helper = helper[:len(helper)-1]
            
        return helper




def run_test(strs, expected, test_name):
    sol = Solution()
    result = sol.longestCommonPrefix(strs)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   strs    :", strs)
        print("   expected:", repr(expected))
        print("   got     :", repr(result))


def main():
    tests = [

        # 🔹 Basic
        (["flower","flow","flight"], "fl", "basic"),

        # 🔹 No common prefix
        (["dog","racecar","car"], "", "no_common_prefix"),

        # 🔹 All identical
        (["same","same","same"], "same", "all_identical"),

        # 🔹 Single string
        (["alone"], "alone", "single_string"),

        # 🔹 Empty array
        ([], "", "empty_array"),

        # 🔹 Contains empty string
        (["","abc","abcd"], "", "contains_empty"),

        # 🔹 Shortest string defines prefix
        (["abc","abcd","ab"], "ab", "shortest_prefix"),

        # 🔹 One char prefix
        (["a","ab","ac"], "a", "single_char_prefix"),

        # 🔹 Case sensitivity
        (["Test","test"], "", "case_sensitive"),

        # 🔹 Prefix at full length of shortest
        (["interview","internet","internal"], "inter", "long_prefix"),

        # 🔹 Mismatch at first char
        (["abc","xbc","ybc"], "", "first_char_mismatch"),

        # 🔹 Two strings
        (["prefix","pre"], "pre", "two_strings"),

        # 🔹 Large input
        (["a"*500 + "x", "a"*500 + "y"], "a"*500, "large_input"),

    ]

    for strs, expected, name in tests:
        run_test(strs, expected, name)


if __name__ == "__main__":
    main()