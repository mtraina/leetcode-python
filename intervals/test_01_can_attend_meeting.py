
import pytest
from ._01_can_attend_meeting import Solution

solution = Solution()

def test_no_overlap():
    intervals = [[0, 30], [35, 50]]
    assert solution.canAttendMeetings(intervals)

def test_overlap():
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert not solution.canAttendMeetings(intervals)

def test_single_interval():
    intervals = [[0, 30]]
    assert solution.canAttendMeetings(intervals)

def test_empty():
    intervals = []
    assert solution.canAttendMeetings(intervals)
