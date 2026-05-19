class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0 
        lst = []
        while i < len(word1) and i <len(word2) :
            lst.append(word1[i])
            lst.append(word2[i])
            i+=1
        if i >= len(word1) and i<len(word2):
            lst.append(word2[i:])
        if i>=len(word2) and i<len(word1):
            lst.append(word1[i:])   
        return "".join(lst)

def run_test(sol: Solution, word1: str, word2: str, expected: str, name: str) -> None:
    try:
        got = sol.mergeAlternately(word1, word2)
        if got == expected:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   word1    = {word1!r}")
            print(f"   word2    = {word2!r}")
            print(f"   expected = {expected!r}")
            print(f"   got      = {got!r}")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement mergeAlternately ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        ("abc", "pqr", "apbqcr", "equal_length_basic"),
        ("ab", "pqrs", "apbqrs", "word2_longer"),
        ("abcd", "pq", "apbqcd", "word1_longer"),
        ("", "xyz", "xyz", "word1_empty"),
        ("xyz", "", "xyz", "word2_empty"),
        ("a", "b", "ab", "single_chars"),
        ("a", "bcdef", "abcdef", "word2_much_longer"),
        ("hello", "WORLD", "hWeOlRlLoD", "mixed_case"),
        ("111", "2222", "1212122", "digits_as_chars"),
        ("!@#", "$%", "!$@%#", "symbols"),
    ]

    for w1, w2, expected, name in tests:
        run_test(sol, w1, w2, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
