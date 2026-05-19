from __future__ import annotations
from typing import Optional, List, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0

            total = v1 + v2 + carry

            cur.next = ListNode(total % 10)
            cur = cur.next

            carry = total // 10

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        lstNodes = dummy
        rest = 0
        while l1 is not None or l2 is not None or rest != 0:
            rest = l1.val + l2.val + rest
            if rest >= 10 :
                print ( rest , rest-10)
                lstNodes.next = ListNode(rest%10)
                rest = rest // 10
            else :
                print ("else part" , rest)
                lstNodes.next = ListNode(rest)
                rest = 0
            lstNodes = lstNodes.next
            l1 = l1.next
            l2 = l2.next
        
        if l1.next and l2.next is None :
            while l1.next:
                rest = l1.val + rest
                if rest >= 10 :
                    print ("l1 part" , rest)
                    lstNodes.next = ListNode(rest%10)
                    rest = rest // 10
                    print ("l1 part" , rest)

                else :
                    print ("l1 else part" , rest)
                    lstNodes.next = ListNode(rest)
                    rest = 0
                l1 = l1.next
                lstNodes = lstNodes.next


        if l2.next is not None and l1.next is None :
            while l2.next:
                rest = l2.val + rest
                if rest >= 10 :
                    lstNodes.next = ListNode(rest%10)
                    rest = rest // 10
                else :
                    lstNodes.next = ListNode(rest)
                    rest = 0
                l2 = l2.next
                lstNodes = lstNodes.next

        if l1.next is None and l2.next is None and rest != 0:
            lstNodes.next = ListNode(l1.val+l2.val+rest)

        return dummy.next
        
            
               
            




# ----------------------------
# Helpers
# ----------------------------
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """Builds a linked list from python list and returns head."""
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode], limit: int = 1000) -> List[int]:
    """Converts linked list to python list. limit avoids infinite loops."""
    out = []
    cur = head
    steps = 0
    while cur is not None and steps < limit:
        out.append(cur.val)
        cur = cur.next
        steps += 1
    if steps >= limit:
        raise RuntimeError("Linked list seems too long / possible cycle.")
    return out

def assert_equal(got: List[int], expected: List[int], name: str) -> None:
    if got == expected:
        print(f"✅ PASS: {name}")
    else:
        print(f"❌ FAIL: {name}")
        print(f"   got     = {got}")
        print(f"   expected= {expected}")

def run_case(sol: Solution, l1: List[int], l2: List[int], expected: List[int], name: str) -> None:
    head1 = build_linked_list(l1)
    head2 = build_linked_list(l2)
    res = sol.addTwoNumbers(head1, head2)
    got = linked_list_to_list(res)
    assert_equal(got, expected, name)


# ----------------------------
# Main (VSCode friendly)
# ----------------------------
def main():
    sol = Solution()

    # Test cases for LeetCode "Add Two Numbers"
    # Each list represents the number in reverse order.
    cases: List[Tuple[List[int], List[int], List[int], str]] = [
        # basic sample-style
        ([2, 4, 3], [5, 6, 4], [7, 0, 8], "basic_342_plus_465"),

        # carry at last digit extends length
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1], "carry_extends_length"),

        # one is zero
        ([0], [0], [0], "both_zero"),
        ([0], [7, 3], [7, 3], "zero_plus_number"),

        # different lengths, carry in the middle
        ([9, 9], [1], [0, 0, 1], "99_plus_1"),
        ([1, 8], [0], [1, 8], "number_plus_zero"),

        # long carry chain
        ([9, 9, 9], [1], [0, 0, 0, 1], "999_plus_1"),

        # no carry, different lengths
        ([3], [7, 8, 9], [0, 9, 9], "3_plus_987"),

        # random-ish
        ([5, 1, 6], [5, 9, 2], [0, 1, 9], "615_plus_295"),
    ]

    for l1, l2, expected, name in cases:
        try:
            run_case(sol, l1, l2, expected, name)
        except NotImplementedError:
            print("🛑 NotImplementedError: Implement addTwoNumbers ואז תריץ שוב.")
            break
        except Exception as e:
            print(f"💥 EXCEPTION in {name}: {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
