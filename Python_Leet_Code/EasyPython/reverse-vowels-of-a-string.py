class Solution:
    def reverseVowels(self, s: str) -> str:
        if s == "":
            return s
        lst = list(s)
        start = 0
        end = len(s)-1
        setLetters = {'a', 'e', 'i', 'o','u','A', 'E', 'I', 'O','U'}
        while start < end:
            if (lst[start] in setLetters) and (lst[end] in setLetters) :
                k = lst[start]
                lst[start] = lst[end]
                lst[end] = k
                start+=1
                end-=1
            elif lst[start] in setLetters : 
                end-=1
            elif lst[end] in setLetters :
                start+=1
            else:
                start+=1
                end-=1

        return "".join(lst)


def run_test(sol, s, expected, name):
    try:
        got = sol.reverseVowels(s)
        if got == expected:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   input    = {s!r}")
            print(f"   expected = {expected!r}")
            print(f"   got      = {got!r}")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement reverseVowels ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # official style
        ("hello", "holle", "basic_1"),
        ("leetcode", "leotcede", "basic_2"),

        # single char
        ("a", "a", "single_vowel"),
        ("b", "b", "single_consonant"),

        # empty string
        ("", "", "empty_string"),

        # all vowels
        
        ("aeiou", "uoiea", "all_lower_vowels"),
        ("AEIOU", "UOIEA", "all_upper_vowels"),
        ("AEIOU", "UOIEA", "all_upper_vowels"),


        # mixed case
        ("aA", "Aa", "mixed_case_two"),
        ("hEllO", "hOllE", "mixed_case_word"),

        # no vowels
        ("rhythm", "rhythm", "no_vowels"),

        # vowels at edges
        ("ab", "ab", "vowel_then_consonant"),
        ("ba", "ba", "consonant_then_vowel"),

        # complex
        ("Programming", "Prigrammong", "complex_case_1"),
        ("Reverse Vowels", "Revorse Vewels", "complex_case_2"),
    ]

    for s, expected, name in tests:
        run_test(sol, s, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
