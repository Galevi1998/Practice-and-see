from typing import List

class Solution:
    def evaluate(self, s, knowledge):
        d = {k:v for k, v in knowledge}
        print(d)
        t = s.split("(")
        print(t)
        ans = t[0]
        for i in range(1, len(t)):
            a, b = t[i].split(")")
            print(t[i].split(")"))
            print(b)
            ans += d.get(a, "?") + b
            print ( ans)
        return ans
        
    
def main():
    sol = Solution()
    nums = "(name)is(age)yearsold"

    print("Original list:", nums)

    k = sol.evaluate(nums,[["name","bob"],["age","two"]])
    
    print("Number of unique elements:", k)

if __name__ == "__main__":
    main()