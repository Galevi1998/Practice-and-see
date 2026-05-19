from typing import Optional, List
from collections import deque

#Im gal and im the best
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node :
            return None
        newGraph = {}
        visited = set()
        queue = deque([node])
        while queue :
            currentNeigbors = queue.popleft().neighbors
            if currentNeigbors is None:
                return None
            print(len(currentNeigbors))
            maybeNew = []
            for i in currentNeigbors:
                if i.val not in visited:
                    newNode = Node(i.val,i.neighbors)
                    maybeNew.append(newNode)
                    queue.append(i)
                    visited.add(i.val)
            if maybeNew != [] :
                newGraph.append(maybeNew)
            print(newGraph)
            print("finished")
        return newGraph


def build_graph(adj_list):
    if not adj_list:
        return None

    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}

    for i, neighbors in enumerate(adj_list, start=1):
        nodes[i].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]


def graph_to_adj_list(node):
    if not node:
        return []

    visited = {}
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        if curr.val in visited:
            continue

        visited[curr.val] = sorted([nei.val for nei in curr.neighbors])

        for nei in curr.neighbors:
            if nei.val not in visited:
                queue.append(nei)

    max_val = max(visited.keys())
    return [visited.get(i, []) for i in range(1, max_val + 1)]


def is_deep_clone(original, cloned):
    if original is None and cloned is None:
        return True
    if original is None or cloned is None:
        return False
    if original is cloned:
        return False

    visited = set()
    queue = deque([(original, cloned)])

    while queue:
        o, c = queue.popleft()

        if o is c:
            return False

        if o.val != c.val:
            return False

        if len(o.neighbors) != len(c.neighbors):
            return False

        if id(o) in visited:
            continue

        visited.add(id(o))

        for on, cn in zip(o.neighbors, c.neighbors):
            queue.append((on, cn))

    return True


def run_test(adj_list, expected, test_name):
    sol = Solution()
    original = build_graph(adj_list)
    cloned = sol.cloneGraph(original)

    result_adj = graph_to_adj_list(cloned)

    if result_adj == expected and is_deep_clone(original, cloned):
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   adj_list :", adj_list)
        print("   expected :", expected)
        print("   got      :", result_adj)
        print("   deep copy:", is_deep_clone(original, cloned))


def main():
    tests = [

        (
            [[2,4],[1,3],[2,4],[1,3]],
            [[2,4],[1,3],[2,4],[1,3]],
            "square_cycle"
        ),

        (
            [[]],
            [[]],
            "single_node_no_neighbors"
        ),

        (
            [],
            [],
            "empty_graph"
        ),

        (
            [[2],[1]],
            [[2],[1]],
            "two_nodes_connected"
        ),

        (
            [[2],[3],[4],[1]],
            [[2],[3],[4],[1]],
            "directed_style_cycle_local"
        ),

        (
            [[2,3],[1,3],[1,2]],
            [[2,3],[1,3],[1,2]],
            "triangle_cycle"
        ),

        (
            [[2,3,4],[1],[1],[1]],
            [[2,3,4],[1],[1],[1]],
            "star_graph"
        ),
    ]

    for adj_list, expected, name in tests:
        run_test(adj_list, expected, name)


if __name__ == "__main__":
    main()