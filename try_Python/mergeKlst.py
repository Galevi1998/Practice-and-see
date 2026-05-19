from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for node in lists:
            while node != None :
                arr.append(node.val)
                node = node.next
        sorted(arr)
        return build_linked_list(arr)
        

def build_linked_list(values):
    """Creates a linked list from a list of integers."""
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Prints the values in a linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

def main():
    lists1 = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]

    # Test case 2: Some empty lists
    lists2 = [
        build_linked_list([]),
        build_linked_list([1]),
        build_linked_list([])
    ]

    # Test case 3: All lists are empty
    lists3 = []

    # Create solution instance
    sol = Solution()

    print("Merged List 1:")
    print_linked_list(sol.mergeKLists(lists1))  # Expected: [1, 1, 2, 3, 4, 4, 5, 6] after implementation

    print("Merged List 2:")
    print_linked_list(sol.mergeKLists(lists2))  # Expected: [1] after implementation

    print("Merged List 3:")
    print_linked_list(sol.mergeKLists(lists3))  # Expected: [] after implementation

if __name__ == "__main__":
    main()
