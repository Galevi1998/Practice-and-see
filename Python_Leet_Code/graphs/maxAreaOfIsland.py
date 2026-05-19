from typing import List
from collections import deque
import copy


class Solution:

    def islandSize(self, grid: List[List[int]] , r, c, R, C, visited:set, islandQueue) -> int:
        dirRow = [1 ,-1, 0, 0]
        dirCol = [0, 0, 1 ,-1]
        islandS = 1
        while islandQueue:
            current = islandQueue.popleft()
            for i in range(4) : 
                rr = current[0] + dirRow[i]
                cc = current[1] + dirCol[i]
                if rr<0 or cc<0 : continue
                if rr>=R or cc >= C : continue
                if (rr,cc) in visited : continue
                if grid[rr][cc] != 1: continue
                islandS = islandS+1
                visited.add((rr,cc))
                islandQueue.append((rr,cc))

        return islandS


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        if R <= 0 : 
            return 0 
        C = len(grid[0])
        visited = set()
        islandQueue = deque()
        bigestIsland = 0
        for r in range(R):
            for c in range(C):
                if(grid[r][c] == 1 and (r,c) not in visited):
                    visited.add((r,c))
                    islandQueue.append((r,c))
                    islandS = self.islandSize(grid,r,c,R,C,visited,islandQueue) 
                    if islandS > bigestIsland:
                        bigestIsland = islandS
        return bigestIsland


def run_test(grid, expected, test_name):
    sol = Solution()
    grid_copy = copy.deepcopy(grid)

    result = sol.maxAreaOfIsland(grid_copy)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   grid:")
        for row in grid:
            print("   ", row)
        print("   expected:", expected)
        print("   got     :", result)


def main():
    tests = [

        (
            [
                [0,0,1,0,0],
                [0,1,1,1,0],
                [0,0,1,0,0],
            ],
            5,
            "cross_island_area_5"
        ),

        (
            [
                [1,1,0,0],
                [1,0,0,1],
                [0,0,1,1],
            ],
            3,
            "two_islands_same_area_3"
        ),

        (
            [
                [0,0,0],
                [0,0,0],
            ],
            0,
            "all_water"
        ),

        (
            [
                [1,1,1],
                [1,1,1],
            ],
            6,
            "all_land"
        ),

        (
            [[1]],
            1,
            "single_land"
        ),

        (
            [[0]],
            0,
            "single_water"
        ),

        (
            [
                [1,0,1],
                [0,1,0],
                [1,0,1],
            ],
            1,
            "diagonal_not_connected"
        ),

        (
            [[1,1,0,1,1,1]],
            3,
            "single_row"
        ),

        (
            [
                [1],
                [1],
                [0],
                [1],
                [1],
                [1],
            ],
            3,
            "single_column"
        ),

        (
            [
                [1,1,1],
                [1,0,1],
                [1,1,1],
            ],
            8,
            "donut_shape"
        ),

        (
            [],
            0,
            "empty_grid_local"
        ),
    ]

    for grid, expected, name in tests:
        run_test(grid, expected, name)


if __name__ == "__main__":
    main()