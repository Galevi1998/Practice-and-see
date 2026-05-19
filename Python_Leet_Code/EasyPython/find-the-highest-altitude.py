from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0 
        diffAlt = 0
        for i in gain:
            diffAlt += i
            if diffAlt>maxAlt:
                maxAlt = diffAlt
        return maxAlt


def run_test(sol: Solution, gain: List[int], expected: int, name: str) -> None:
    try:
        got = sol.largestAltitude(gain)
        if got == expected:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   gain     = {gain}")
            print(f"   expected = {expected}")
            print(f"   got      = {got}")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement largestAltitude ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # official-style examples
        ([-5, 1, 5, 0, -7], 1, "example_1"),
        ([-4, -3, -2, -1, 4, 3, 2], 0, "example_2"),

        # edge cases
        ([], 0, "empty_gain_n0"),             # n=0 => only point 0 altitude 0
        ([0, 0, 0], 0, "all_zeros"),
        ([1, 2, 3], 6, "all_positive"),
        ([-1, -2, -3], 0, "all_negative"),

        # mixed
        ([2, -1, 2, -1, 2], 4, "zigzag_positive"),
        ([-1, 5, -2, 3, -10, 6], 5, "mixed_peaks"),
        ([10, -5, -5], 10, "peak_at_first_move"),
        ([-2, 2], 0, "returns_to_zero"),
    ]

    for gain, expected, name in tests:
        run_test(sol, gain, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
