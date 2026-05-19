



class Solution:
    def isPalindrome(self, x: int) -> bool:
        length = len(str(x))
        print(x)
        if x%10 != x//(10 ** (length - 1)):
            return False
        y = x%(10 ** (length - 1))//10
        if length >1 :
            return self.isPalindrome(y)
        return True


def run_test(sol, x, expected, name):
    try:
        result = sol.isPalindrome(x)
        if result == expected:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   input    = {x}")
            print(f"   expected = {expected}")
            print(f"   got      = {result}")
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # basic palindromes
        (1000021, False, "odd_length_palindrome"),
        (1221, True, "even_length_palindrome"),
        (7, True, "single_digit"),

        # non-palindromes
        (123, False, "simple_non_palindrome"),
        (10, False, "ends_with_zero"),
        (100, False, "ends_with_zeros"),

        # negatives
        (-121, False, "negative_palindrome_like"),
        (-1, False, "negative_single_digit"),

        # edge cases
        (0, True, "zero"),
        (11, True, "double_digit_palindrome"),
        (12, False, "double_digit_non_palindrome"),

        # large numbers
        (123454321, True, "large_palindrome"),
        (123456789, False, "large_non_palindrome"),
    ]

    for x, expected, name in tests:
        run_test(sol, x, expected, name)


if __name__ == "__main__":
    main()
