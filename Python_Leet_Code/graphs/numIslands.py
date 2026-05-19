from typing import List
from collections import deque
import copy


class Solution:
    def exploreNeighbors(self, grid:List[List[str]],r,c,visited, R , C) -> None:
        dr = [1,-1,0,0]
        dc = [0,0,1,-1]
        queue = deque([(r,c)])
        visited.add((r,c))
        while queue :
            now = queue.popleft()
            for i in range(4):
                rr = now[0]+dr[i]
                cc = now[1]+dc[i]
                if rr<0 or cc<0 : continue
                if cc>=C or rr >=R : continue

                if (rr,cc) in visited : continue
                if grid[rr][cc] == '0' : continue

                visited.add((rr,cc))
                queue.append((rr,cc))

        
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        if R<=0 : return 0
        C = len(grid[0])
        rIter,cIter = 0,0
        visited = set()
        numOfIslands = 0
        for rIter in range(R):
            for cIter in range(C):
                if grid[rIter][cIter] == '1' and (rIter,cIter) not in visited :
                    numOfIslands+=1
                    self.exploreNeighbors(grid,rIter,cIter,visited,R,C)
                
                

        return numOfIslands


def run_test(grid, expected, test_name):
    sol = Solution()
    grid_copy = copy.deepcopy(grid)

    result = sol.numIslands(grid_copy)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   grid    :")
        for row in grid:
            print("   ", row)
        print("   expected:", expected)
        print("   got     :", result)


def main():
    tests = [

        # 🔹 Basic one island
        (
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1,
            "basic_one_island"
        ),

        # 🔹 Multiple islands
        (
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3,
            "multiple_islands"
        ),

        # 🔹 All water
        (
            [
                ["0","0","0"],
                ["0","0","0"]
            ],
            0,
            "all_water"
        ),

        # 🔹 All land
        (
            [
                ["1","1","1"],
                ["1","1","1"],
                ["1","1","1"]
            ],
            1,
            "all_land"
        ),

        # 🔹 Single land cell
        (
            [["1"]],
            1,
            "single_land"
        ),

        # 🔹 Single water cell
        (
            [["0"]],
            0,
            "single_water"
        ),

        # 🔹 Diagonal land does NOT connect
        (
            [
                ["1","0","1"],
                ["0","1","0"],
                ["1","0","1"]
            ],
            5,
            "diagonal_not_connected"
        ),

        # 🔹 Thin row
        (
            [["1","0","1","1","0","1"]],
            3,
            "single_row"
        ),

        # 🔹 Thin column
        (
            [
                ["1"],
                ["0"],
                ["1"],
                ["1"],
                ["0"],
                ["1"]
            ],
            3,
            "single_column"
        ),

        # 🔹 Donut shape, still one island
        (
            [
                ["1","1","1"],
                ["1","0","1"],
                ["1","1","1"]
            ],
            1,
            "donut_one_island"
        ),

        # 🔹 Empty grid local edge case
        (
            [],
            0,
            "empty_grid"
        ),
    ]

    for grid, expected, name in tests:
        run_test(grid, expected, name)


if __name__ == "__main__":
    main()