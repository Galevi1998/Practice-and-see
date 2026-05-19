import math

# ====== Simulated LeetCode API ======

pick = None  # הערך הסודי יוגדר בכל טסט

def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


# ====== Solution Template ======

class Solution:
    def guessNumber(self, n: int) -> int:
        low =1 
        big = n
        decision = guess(n)
        i=0
        while decision != 0 :
            mid = (low+big)//2

            decision = guess(mid)
            if decision == 0 :
                return mid
            elif decision == 1:
                low = mid
            else:
                big = mid
        return n

            
                




# ====== Testing Framework ======

def run_test(n, secret, test_name):
    global pick
    pick = secret

    sol = Solution()
    result = sol.guessNumber(n)

    if result == secret:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   n       :", n)
        print("   secret  :", secret)
        print("   got     :", result)


def main():
    tests = [

        # 🔹 Basic middle
        (10, 6, "middle_case"),

        # 🔹 First number
        (10, 1, "lower_boundary"),

        # 🔹 Last number
        (10, 10, "upper_boundary"),

        # 🔹 Single possible number
        (1, 1, "single_number"),

        # 🔹 Large n, small pick
        (1_000_000, 3, "large_n_small_pick"),

        # 🔹 Large n, large pick
        (1_000_000, 999_999, "large_n_large_pick"),

        # 🔹 Large n, middle pick
        (1_000_000, 500_000, "large_n_middle_pick"),

        # 🔹 Power of two boundary
        (1024, 1024, "power_of_two_upper"),

        # 🔹 Another random mid
        (100, 73, "random_mid"),

    ]

    for n, secret, name in tests:
        run_test(n, secret, name)


if __name__ == "__main__":
    main()
