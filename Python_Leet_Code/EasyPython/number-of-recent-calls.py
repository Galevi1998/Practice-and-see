from collections import deque
import time

class RecentCounter:

    def __init__(self):
        self.queueTime = deque()

    def ping(self, t: int) -> int:
        self.queueTime.append(t)
        que = self.queueTime
        while que[0] < t-3000 :
            que.popleft()
        return len(que)
        


def run_test(operations, expected, test_name):
    obj = None
    results = []

    for op in operations:
        if op[0] == "RecentCounter":
            obj = RecentCounter()
            results.append(None)
        elif op[0] == "ping":
            results.append(obj.ping(op[1]))

    if results == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   operations:", operations)
        print("   expected  :", expected)
        print("   got       :", results)


def main():
    tests = [

        # 🔹 Basic example from LeetCode
        (
            [
                ["RecentCounter"],
                ["ping", 1],
                ["ping", 100],
                ["ping", 3001],
                ["ping", 3002],
            ],
            [None, 1, 2, 3, 3],
            "basic_example"
        ),

        # 🔹 All within 3000 window
        (
            [
                ["RecentCounter"],
                ["ping", 1],
                ["ping", 2],
                ["ping", 3],
                ["ping", 4],
            ],
            [None, 1, 2, 3, 4],
            "all_within_window"
        ),

        # 🔹 Window fully shifts
        (
            [
                ["RecentCounter"],
                ["ping", 1000],
                ["ping", 4000],
                ["ping", 7000],
                ["ping", 10000],
            ],
            [None, 1, 1, 1, 1],
            "window_fully_shifts"
        ),

        # 🔹 Boundary exactly 3000
        (
            [
                ["RecentCounter"],
                ["ping", 1],
                ["ping", 3001],  # includes 1
                ["ping", 6001],  # includes 3001
            ],
            [None, 1, 2, 2],
            "exact_boundary"
        ),

        # 🔹 Large jumps
        (
            [
                ["RecentCounter"],
                ["ping", 1],
                ["ping", 10000],
                ["ping", 20000],
                ["ping", 30000],
            ],
            [None, 1, 1, 1, 1],
            "large_jumps"
        ),

        # 🔹 Many clustered then jump
        (
            [
                ["RecentCounter"],
                ["ping", 1],
                ["ping", 100],
                ["ping", 200],
                ["ping", 300],
                ["ping", 4000],
            ],
            [None, 1, 2, 3, 4, 1],
            "cluster_then_reset"
        ),

        # 🔹 Dense near boundary
        (
            [
                ["RecentCounter"],
                ["ping", 1000],
                ["ping", 2000],
                ["ping", 3000],
                ["ping", 4000],
            ],
            [None, 1, 2, 3, 4],
            "dense_boundary_case"
        ),

    ]

    for operations, expected, name in tests:
        run_test(operations, expected, name)


if __name__ == "__main__":
    main()
