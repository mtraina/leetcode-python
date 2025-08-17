from typing import List

class Solution:

    def canAttendMeetings(self, intervals: List[List[int]]):
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            """ if the start of the current element is before the end of the previous element, 
            there is conflict"""
            if intervals[i][0] < intervals[i-1][1]:
                return False
                       
        return True