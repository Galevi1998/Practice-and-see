from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        print(maxCandies)
        lstBool = []
        for i in candies:
            if maxCandies <= i+extraCandies :
                lstBool.append(True)
            else:
                lstBool.append(False)
        return lstBool
        


def run_test(sol: Solution, candies: List[int], extra: int, expected: List[bool], name: str) -> None:
    try:
        got = sol.kidsWithCandies(candies, extra)
        if got == expected:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   candies  = {candies}")
            print(f"   extra    = {extra}")
            print(f"   expected = {expected}")
            print(f"   got      = {got}")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement kidsWithCandies ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # official-style examples
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True], "basic_example"),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False], "one_extra"),
        ([12, 1, 12], 10, [True, False, True], "large_extra"),

        # edge cases
        ([1], 0, [True], "single_child_no_extra"),
        ([1], 5, [True], "single_child_with_extra"),
        ([5, 5, 5], 0, [True, True, True], "all_equal_no_extra"),
        ([5, 5, 5], 1, [True, True, True], "all_equal_with_extra"),

        # tricky-ish
        ([1, 2, 3, 4], 0, [False, False, False, True], "already_has_max"),
        ([1, 2, 3, 4], 1, [False, False, True, True], "some_reach_max"),
    ]

    for candies, extra, expected, name in tests:
        run_test(sol, candies, extra, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
