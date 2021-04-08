class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0
        starts = [ii[0] for ii in sorted(intervals, key = lambda x: x[0])]
        ends = [ii[1] for ii in sorted(intervals, key = lambda x: x[1])]
        rooms = 0
        start = 0
        end = 0
        while start < len(intervals):
            if starts[start] >= ends[end]:
                end += 1
                rooms -= 1
            start += 1
            rooms += 1
        return rooms
            
        
        
        # if not intervals:
        #     return 0
        # sorted_rms = sorted(intervals, key = lambda x: x[0])
        # ending_rms = []
        # heapq.heappush(ending_rms, sorted_rms[0][1])
        # for rm in sorted_rms[1:]:
        #     if rm[0] >= ending_rms[0]:
        #         heapq.heappop(ending_rms)
        #     heapq.heappush(ending_rms, rm[1]) 
        # return len(ending_rms)
        
        
        
#         # If there is no meeting to schedule then no room needs to be allocated.
#         if not intervals:
#             return 0

#         # The heap initialization
#         free_rooms = []

#         # Sort the meetings in increasing order of their start time.
#         intervals.sort(key= lambda x: x[0])

#         # Add the first meeting. We have to give a new room to the first meeting.
#         heapq.heappush(free_rooms, intervals[0][1])

#         # For all the remaining meeting rooms
#         for room in intervals[1:]:

#             # If the room due to free up the earliest is free, assign that room to this meeting.
#             if room[0] >= free_rooms[0]:
#                 heapq.heappop(free_rooms)

#             # If a new room is to be assigned, then also we add to the heap,
#             # If an old room is allocated, then also we have to add to the heap with updated end time.
#             heapq.heappush(free_rooms, room[1])

#         # The size of the heap tells us the minimum rooms required for all the meetings.
#         return len(free_rooms)  



#         # If there are no meetings, we don't need any rooms.
#         if not intervals:
#             return 0

#         used_rooms = 0
#         start_timings = sorted([i[0] for i in intervals])
#         end_timings = sorted(i[1] for i in intervals)
#         L = len(intervals)
#         end_pointer = 0
#         start_pointer = 0
#         while start_pointer < L:
#             if start_timings[st9art_pointer] >= end_timings[end_pointer]:
#                 used_rooms -= 1
#                 end_pointer += 1
#             used_rooms += 1    
#             start_pointer += 1   
#         return used_rooms