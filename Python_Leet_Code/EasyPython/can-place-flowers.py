from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:        
        isLeftPrevFlower = False
        lengthOfFlowrs= len(flowerbed)
        if lengthOfFlowrs == 1 and flowerbed[0] == 0:
            return True
        for i in range(lengthOfFlowrs):
            print(i,"index")
            print(flowerbed)
            print("is left is 1 ?",isLeftPrevFlower)
            if flowerbed[i]==1 : 
                isLeftPrevFlower = True
                continue
            if i==0: 
                if flowerbed[i+1] == 0:
                    print("change")
                    flowerbed[i] = 1
                    n=n-1
                    isLeftPrevFlower = True
                continue
            if flowerbed[i]==0 and isLeftPrevFlower==False:
                print("change")
                flowerbed[i] = 1
                n=n-1
                isLeftPrevFlower = True

            else:
                isLeftPrevFlower = False

            print(flowerbed)
        return n<=0



            
            










        
        # if n<=0:
        #     return True
        # lenBeds = len(flowerbed)
        # i = 0
        # while i < lenBeds:
        #     if(flowerbed[i]==0):
        #         isRight = i == lenBeds-1 or flowerbed[i+1] == 0
        #         isLeft = i == 0 or flowerbed[i-1]==0
        #         if(isRight and isLeft):
        #             n=n-1
        #             flowerbed[i]=1
        #             i+=2
        #         else:
        #             i+=1
        #     else:
        #         i+=1
        # for i in range(lenBeds):
        #     if(flowerbed[i]==0):
        #         isRight = i == lenBeds-1 or flowerbed[i+1] == 0
        #         isLeft = i == 0 or flowerbed[i-1]==0
        #         if(isRight and isLeft):
        #             n=n-1
        #             flowerbed[i]=1
        #             i+=1
        # return n<=0
    
# from dataclasses import dataclass, field
# from typing import List, Dict


#                                                 @dataclass
#                                                 class DeveloperProfile:
#                                                     full_name: str
#                                                     title: str
#                                                     skills: List[str] = field(default_factory=list)
#                                                     education: Dict[str, str] = field(default_factory=dict)
#                                                     projects: List[str] = field(default_factory=list)


#                                                 gal_levi = DeveloperProfile(
#                                                     full_name="Gal Levi",
#                                                     title="Full-Stack & Mobile Developer",
#                                                     skills=[
#                                                         "Python","NextJS","React","Node.js","SwiftUI","Kotlin Multiplatform",
#                                                         "Firebase","TypeScript","MongoDB","JavaScript","Computer Vision",
#                                                     ],
#                                                     education={
#                                                         "institution": "The College of Management Academic Studies",
#                                                         "degree": "B.Sc. Computer Science",
#                                                     },
#                                                 )


def run_test(sol: Solution, flowerbed: List[int], n: int, expected: bool, name: str) -> None:
    try:
        # copy to avoid mutation side-effects affecting prints / expected comparisons
        fb_copy = flowerbed[:]
        got = sol.canPlaceFlowers(fb_copy, n)

        if got == expected:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   flowerbed = {flowerbed}")
            print(f"   n         = {n}")
            print(f"   expected  = {expected}")
            print(f"   got       = {got}")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement canPlaceFlowers ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # common examples
        ([1, 0, 0, 0, 1], 1, True, "example_true_1"),
        ([1, 0, 0, 0, 1], 2, False, "example_false_2"),

        # edge: n = 0 always true
        ([1, 0, 1], 0, True, "n_zero"),

        # single slot
        ([0], 1, True, "single_empty_place_1"),
        ([0], 2, False, "single_empty_place_2"),
        ([1], 1, False, "single_taken_place"),

        # all empty
        ([0, 0], 1, True, "two_empty_place_1"),
        ([0, 0], 2, False, "two_empty_place_2"),
        ([0, 0], 3, False, "two_empty_place_3"),

        ([0, 0, 0], 1, True, "three_empty_place_1"),
        ([0, 0, 0], 2, True, "three_empty_place_2"),
        ([0, 0, 0], 3, False, "three_empty_place_3"),

        # starts/ends with ones
        ([1, 0, 0, 0], 1, True, "starts_with_one"),
        ([0, 0, 0, 1], 1, True, "ends_with_one"),
        ([1, 0, 0, 1], 1, False, "blocked_middle"),

        # alternating
        ([0, 1, 0, 1, 0], 1, False, "alternating_no_space"),
        ([0, 0, 1, 0, 0], 2, True, "two_sides_can_place_2"),
        ([0, 0, 1, 0, 0], 3, False, "two_sides_cannot_place_3"),

        # tricky gaps
        ([0, 0, 0, 0, 0], 3, True, "all_zero_len5_place3"),
        ([1, 0, 0, 0, 0, 1], 2, False, "ones_at_edges_len6"),
        # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ]

    for flowerbed, n, expected, name in tests:
        run_test(sol, flowerbed, n, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
