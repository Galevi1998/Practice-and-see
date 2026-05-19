class Solution:
    def isPalindrome(self, s: str) -> bool:
        Strip = s.replace(" " ,"")
        lenStr = len(Strip)
        Strip = "".join(ch for ch in s if ch.isalpha() and ch.isascii()).lower()
        i , end=0 , len(Strip)-1
        
        print(Strip)
        while i<end :
            if Strip[i] != Strip[end] :
                return False
            i+=1
            end-=1
        return True


def run_test(s, expected, test_name):
    sol = Solution()
    result = sol.isPalindrome(s)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   s       :", repr(s))
        print("   expected:", expected)
        print("   got     :", result)


def main():
    tests = [

        # 🔹 Classic examples
        ("A man, a plan, a canal: Panama", True, "classic_true"),
        ("race a car", False, "classic_false"),
        (" ", True, "single_space_true"),

        # 🔹 Empty string
        ("", True, "empty_string_true"),

        # 🔹 Only punctuation
        ("!!!", True, "only_punct_true"),

        # 🔹 Mixed case
        ("Aa", True, "mixed_case_true"),

        # 🔹 Digits
        ("0P", False, "digit_letter_false"),
        ("12321", True, "digits_pal_true"),
        ("1231", False, "digits_pal_false"),

        # 🔹 Underscore & symbols (underscore is NOT alphanumeric)
        ("ab_a", True, "underscore_ignored_true"),

        # 🔹 Palindrome with lots of noise
        (".,,A,,. ", True, "noise_true"),

        # 🔹 Even/odd length after cleaning
        ("No 'x' in Nixon", True, "odd_cleaned_true"),
        ("Red rum, sir, is murder", True, "even_cleaned_true"),

        # 🔹 Non-pal due to one mismatch after cleaning
        ("ab@c#d!a", False, "single_mismatch_false"),

        # 🔹 Very long (stress-ish)
        ("a"*5000 + "b" + "a"*5000, True, "very_long_true"),

    ]

    for s, expected, name in tests:
        run_test(s, expected, name)


if __name__ == "__main__":
    main()