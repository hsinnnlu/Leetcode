from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events_by_start = sorted(events, key=lambda x: x[0])
        events_by_end = sorted(events, key=lambda x: x[1])

        ans = 0
        max_prev = 0
        j = 0
        n = len(events)

        for start, end, value in events_by_start:
            while j < n and events_by_end[j][1] < start:
                max_prev = max(max_prev, events_by_end[j][2])
                j += 1
            ans = max(ans, value, value + max_prev)

        return ans


if __name__ == "__main__":
    s = Solution()
    events = [[1,3,2],[4,5,2],[1,5,5]]
    print(s.maxTwoEvents(events))
