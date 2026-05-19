from typing import List
from collections import deque
import copy


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R =  len(image)
        C = len(image[0])
        dirRow = [1,-1,0,0]
        dirCol = [0,0,1,-1]
        visited = set()
        neighbors = deque()
        neighbors.append((sr,sc))
        value = image[sr][sc]
        ite = 0
        while neighbors:
            ite +=1
            current = neighbors.popleft()
            visited.add(current)
            for i in range(4):
                rr = current[0] + dirRow[i]
                cc = current[1] + dirCol[i]
                if rr < 0 or cc < 0 : continue
                if rr >= R or cc >= C : continue
                if (rr,cc) in visited : 
                    continue
                if image[rr][cc] != value : 
                    continue
                visited.add((rr,cc))
                neighbors.append((rr,cc))
                image[rr][cc] = color

        image[sr][sc] = color
        return image


def run_test(image, sr, sc, color, expected, test_name):
    sol = Solution()
    image_copy = copy.deepcopy(image)

    result = sol.floodFill(image_copy, sr, sc, color)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   image   :", image)
        print("   sr, sc  :", sr, sc)
        print("   color   :", color)
        print("   expected:", expected)
        print("   got     :", result)


def main():
    tests = [

        (
            [[1,1,1],[1,1,0],[1,0,1]],
            1, 1, 2,
            [[2,2,2],[2,2,0],[2,0,1]],
            "basic_fill"
        ),

        (
            [[0,0,0],[0,0,0]],
            0, 0, 0,
            [[0,0,0],[0,0,0]],
            "same_color_no_change"
        ),

        (
            [[1]],
            0, 0, 2,
            [[2]],
            "single_cell_change"
        ),

        (
            [[1]],
            0, 0, 1,
            [[1]],
            "single_cell_same_color"
        ),

        (
            [[1,0,1],[0,1,0],[1,0,1]],
            1, 1, 2,
            [[1,0,1],[0,2,0],[1,0,1]],
            "diagonal_not_connected"
        ),

        (
            [[1,1,1,1]],
            0, 2, 9,
            [[9,9,9,9]],
            "single_row_fill"
        ),

        (
            [[1],[1],[0],[1]],
            1, 0, 3,
            [[3],[3],[0],[1]],
            "single_column_partial"
        ),

        (
            [[1,1,0],[1,0,0],[0,0,1]],
            0, 0, 5,
            [[5,5,0],[5,0,0],[0,0,1]],
            "partial_component_fill"
        ),

        (
            [[2,2,2],[2,3,2],[2,2,2]],
            1, 1, 9,
            [[2,2,2],[2,9,2],[2,2,2]],
            "center_isolated"
        ),

    ]

    for image, sr, sc, color, expected, name in tests:
        run_test(image, sr, sc, color, expected, name)


if __name__ == "__main__":
    main()




#     checking this index 2,1 this is the val 0 need to equal 1
# not equal in index 2,1
# checking this index 0,1 this is the val 1 need to equal 1
# lets go 0,1
# lets go 2
# checking this index 1,2 this is the val 0 need to equal 1
# not equal in index 1,2
# checking this index 1,0 this is the val 1 need to equal 1
# lets go 1,0
# lets go 2
# checking this index 2,1 this is the val 0 need to equal 1
# not equal in index 2,1
# checking this index 0,1 this is the val 2 need to equal 1
# visited already in index 0,1
# checking this index 1,2 this is the val 0 need to equal 1
# not equal in index 1,2
# checking this index 1,0 this is the val 2 need to equal 1
# visited already in index 1,0
# checking this index 2,1 this is the val 0 need to equal 1
# not equal in index 2,1
# checking this index 0,1 this is the val 2 need to equal 1
# visited already in index 0,1
# checking this index 1,2 this is the val 0 need to equal 1
# not equal in index 1,2
# checking this index 1,0 this is the val 2 need to equal 1
# visited already in index 1,0