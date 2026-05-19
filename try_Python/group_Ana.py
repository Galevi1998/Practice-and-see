from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictonary = {}
        lstAnag = []
        for str in strs :
            key = ''.join(sorted(str))
            if dictonary.get(key):
                dictonary[key].append(str)
            else:
                dictonary[key] = [str]
        for key in dictonary.keys():
            lstAnag.append(dictonary.get(key))
        return lstAnag

def print_grouped_anagrams(result: List[List[str]]):
    """Prints the list of grouped anagrams."""
    for group in result:
        print(group)

def main():
    # Test case 1: Normal case
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    # Test case 2: All strings are anagrams of each other
    input2 = ["abc", "bca", "cab", "cba"]

    # Test case 3: No anagrams
    input3 = ["dog", "cat", "bird"]

    # Test case 4: Empty input
    input4 = ["a"]

    # Create solution instance
    sol = Solution()

    print("Grouped Anagrams 1:")
    print_grouped_anagrams(sol.groupAnagrams(input1))

    print("Grouped Anagrams 2:")
    print_grouped_anagrams(sol.groupAnagrams(input2))

    print("Grouped Anagrams 3:")
    print_grouped_anagrams(sol.groupAnagrams(input3))

    print("Grouped Anagrams 4:")
    print_grouped_anagrams(sol.groupAnagrams(input4))

if __name__ == "__main__":
    main()
