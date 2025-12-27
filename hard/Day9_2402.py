class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        count = [0] * n      # 每個房間被使用的次數
        timer = [0] * n      # 每個房間目前可用的時間

        itr = 0

        while itr < len(meetings):
            start, end = meetings[itr]
            dur = end - start

            room = -1
            earliest = 10**18
            earliestRoom = -1

            for i in range(n):
                if timer[i] < earliest:
                    earliest = timer[i]
                    earliestRoom = i
                if timer[i] <= start:
                    room = i
                    break

            if room != -1:
                timer[room] = end
                count[room] += 1
            else:
                timer[earliestRoom] += dur
                count[earliestRoom] += 1

            itr += 1

        maxv = 0
        idx = 0
        for i in range(n):
            if count[i] > maxv:
                maxv = count[i]
                idx = i

        return idx


if __name__ == "__main__":
    sol = Solution()

    # 測試資料
    n = 2
    meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]

    result = sol.mostBooked(n, meetings)
    print(result)
