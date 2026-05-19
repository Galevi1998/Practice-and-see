from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        # נקבל True אם שני הרשימות הזהות אותם ערכים וסדר
        a, b = self, other
        while a and b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return a is None and b is None

    def __repr__(self):
        vals = []
        node = self
        while node:
            vals.append(str(node.val))
            node = node.next
        return "->".join(vals)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev



# ====== Helpers לבדיקות ======

def make_list(arr):
    head = None
    prev = None
    for v in arr:
        node = ListNode(v)
        if not head:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head

def run_test(input_list, expected_list, test_name):
    sol = Solution()
    result = sol.reverseList(make_list(input_list))
    expected = make_list(expected_list)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   input    :", input_list)
        print("   expected :", expected_list)
        print("   got      :", result)


def main():
    tests = [

        # 🔹 Normal case
        ([1,2,3,4,5], [5,4,3,2,1], "reverse_normal"),

        # 🔹 Single node
        ([1], [1], "single_node"),

        # 🔹 Empty list
        ([], [], "empty_list"),

        # 🔹 All identical
        ([2,2,2,2], [2,2,2,2], "all_identical"),

        # 🔹 Two elements
        ([1,2], [2,1], "two_elements"),

        # 🔹 Negative numbers
        ([-1,-2,-3], [-3,-2,-1], "negative_numbers"),

        # 🔹 Longer list
        ([10,20,30,40,50,60], [60,50,40,30,20,10], "longer_list"),

    ]

    for inp, exp, name in tests:
        run_test(inp, exp, name)


if __name__ == "__main__":
    main()
