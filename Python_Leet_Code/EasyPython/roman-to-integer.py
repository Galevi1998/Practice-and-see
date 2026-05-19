class Solution:
    def romanToInt(self, s: str) -> int:
        dictLetters = {
            "I": 1,"V": 5,"X" : 10,"L": 50,
            "C" : 100,"D": 500,"M": 1000,
        }
        reducingLetters = {"I","X","C"}
        num = 0
        isReducing = False
        helper = ""
        for i in s :
            current =dictLetters[i] 
            if isReducing and current > dictLetters[helper] : 
                num = num + current - 2*dictLetters[helper] 
                helper = ""
                isReducing = False
            elif i in reducingLetters : 
                helper = i
                isReducing = True
                num += current
            else: 
                helper = ""
                isReducing = False
                num += current
        return num


#אפשר לעשות יותר יעיל


def run_test(s, expected, test_name):
    sol = Solution()
    result = sol.romanToInt(s)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   roman   :", s)
        print("   expected:", expected)
        print("   got     :", result)


def main():
    tests = [

        # 🔹 Basic additive
        ("III", 3, "basic_additive"),

        # 🔹 Simple subtractive
        ("IV", 4, "subtractive_IV"),
        ("IX", 9, "subtractive_IX"),

        # 🔹 Mixed
        ("LVIII", 58, "mixed_example"),

        # 🔹 Complex subtractive
        ("MCMXCIV", 1994, "complex_case"),

        # 🔹 Largest typical value
        ("MMMCMXCIX", 3999, "max_standard"),

        # 🔹 All subtractive pairs
        ("XL", 40, "subtractive_XL"),
        ("XC", 90, "subtractive_XC"),
        ("CD", 400, "subtractive_CD"),
        ("CM", 900, "subtractive_CM"),

        # 🔹 Repeated numerals
        ("XX", 20, "repeated_X"),
        ("CCC", 300, "repeated_C"),

        # 🔹 Edge: smallest
        ("I", 1, "single_I"),

        # 🔹 Edge: subtractive at end
        ("XIV", 14, "subtractive_end"),

        # 🔹 Larger mixed
        ("MMXXIII", 2023, "modern_year"),

        # 🔹 Sequential subtractive cases
        ("CDXLIV", 444, "multiple_subtractive"),

    ]

    for s, expected, name in tests:
        run_test(s, expected, name)


if __name__ == "__main__":
    main()