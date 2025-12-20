from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])

        ans = {0, firstPerson}
        pattern = [i for i in range(n)]

        def find(x):
            if pattern[x] != x:
                pattern[x] = find(pattern[x])
            return pattern[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra != rb:
                pattern[ra] = rb

        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            j = i
            people = set()

            while j < len(meetings) and meetings[j][2] == time:
                x, y, _ = meetings[j]
                union(x, y)
                people.add(x)
                people.add(y)
                j += 1

            secret_member = set()
            for p in people:
                if p in ans:
                    secret_member.add(find(p))

            for p in people:
                if find(p) in secret_member:
                    ans.add(p)

            for p in people:
                pattern[p] = p

            i = j

        return list(ans)


if __name__ == "__main__":
    sol = Solution()
    n = 6
    meetings = [[1,2,5],[2,3,8],[1,5,10]]
    firstPerson = 1

    result = sol.findAllPeople(n, meetings, firstPerson)
    print(result)
