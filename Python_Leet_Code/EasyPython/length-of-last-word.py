class Solution:
    def lengthOfLastWord(self, s: str) -> int:        
        # words = s.split()
        # if not words:
        #     return 0
        # lenWords = len(words)
        # if lenWords == 0 :
        #     return len(words[len(words)])
        
        # print (words[len(words)-1] ,words )
        # return len(words[len(words)-1])
        count =0
                                #when to stop   #steps
        for i in range (len(s) - 1 , -1 ,       -1 ) : 
            while s[i] != " " and i>-1 : 
                count+=1
                i-=1
            if count != 0 :
                return count
        return count


def run_test(s, expected, test_name):
    sol = Solution()
    result = sol.lengthOfLastWord(s)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   s       :", repr(s))
        print("   expected:", expected)
        print("   got     :", result)


def main():
    tests = [

        # 🔹 Basic
        ("Hello World", 5, "basic"),

        # 🔹 Trailing spaces
        ("Hello World   ", 5, "trailing_spaces"),

        # 🔹 Leading spaces
        ("   Hello World", 5, "leading_spaces"),

        # 🔹 Multiple spaces between words
        ("a   b   c", 1, "multiple_spaces_between"),

        # 🔹 Single word
        ("leetcode", 8, "single_word"),

        # 🔹 Only spaces (LeetCode usually won't give this, אבל טוב למקומי)
        ("     ", 0, "only_spaces"),

        # 🔹 Word with punctuation (still non-space chars count)
        ("hi!", 3, "punctuation_single_word"),

        # 🔹 Last word is punctuation-attached
        ("Hello there!!!", 8, "punctuation_last_word"),

        # 🔹 Newlines/tabs count as non-space? (בליטקוד זה בדרך כלל ' ' בלבד, אבל נבדוק קשיחות)
        ("a b\tc", 3, "tab_in_string"),

        # 🔹 Very long last word
        ("x " + "y"*50, 50, "long_last_word"),

        # 🔹 Last word length 1 with trailing spaces
        ("test a   ", 1, "last_word_one_char"),

    ]

    for s, expected, name in tests:
        run_test(s, expected, name)


if __name__ == "__main__":
    main()
