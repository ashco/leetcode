# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
import heapq

def minMeetingRooms(intervals):
    if not intervals: return 0

    intervals.sort(key = lambda x: x[0])

    end_times = []
    heapq.heappush(end_times, intervals[0][1])

    for start, end in intervals[1:]:
        if end_times[0] <= start:
            heapq.heappop(end_times)

        heapq.heappush(end_times, end)

    return len(end_times)


print(minMeetingRooms([[0, 30],[5, 10],[15, 20]])) # 2
print(minMeetingRooms([[7, 10],[2, 4]])) # 1

# --------------------------
# [   ]  [  ]
#   [      ]
#           [  ]