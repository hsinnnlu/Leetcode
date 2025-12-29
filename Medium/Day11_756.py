from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        tab = defaultdict(set)
        for u, v, w in allowed:
            tab[(u, v)].add(w)

        def add_neighbor(node: str) -> List[str]:
            res = ['']
            for i in range(1, len(node)):
                eles = tab[(node[i - 1], node[i])]
                if eles:
                    res = [a + e for e in eles for a in res]
                else:
                    return []
            return res

        visited = set()

        def dfs(node: str) -> bool:
            if len(node) == 1:
                return True
            if node in visited:
                return False

            for nxt in add_neighbor(node):
                if dfs(nxt):
                    return True

            visited.add(node)
            return False

        return dfs(bottom)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    bottom1 = "BCD"
    allowed1 = ["BCG", "CDE", "GEA", "FFF"]
    print(sol.pyramidTransition(bottom1, allowed1))  # Expected: True

    # Example 2
    bottom2 = "AABA"
    allowed2 = ["AAA", "AAB", "ABA", "ABB", "BAC"]
    print(sol.pyramidTransition(bottom2, allowed2))  # Expected: False
