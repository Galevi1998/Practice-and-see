class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myset = set()
        totalS = 0
        totalT = 0
        for ch in s:
            totalS += ord(ch)
            myset.add(ch)
        for ch in t:
            totalT += ord(ch)
            if ch not in myset:
                return False
        if len(s) == len(t) and totalS == totalT:
            return True
        return False




def main():
    sol = Solution()

    # דוגמאות לבדיקה
    test_cases = [
        ("anagram", "nagaram", True),   # כן אנגרמה
        ("rat", "car", False),          # לא אנגרמה
        ("", "", True),                 # שתי מחרוזות ריקות
        ("a", "a", True),               # תו יחיד אותו דבר
        ("ab", "ba", True),             # סיבוב פשוט
        ("hello", "bello", False),      # שונות באות אחת
    ]

    for s, t, expected in test_cases:
        result = sol.isAnagram(s, t)
        print(f"s='{s}', t='{t}' | Output: {result} | Expected: {expected}")


if __name__ == "__main__":
    main()
