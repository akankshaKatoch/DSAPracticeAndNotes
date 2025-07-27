import heapq

def assignMeetingRooms(intervals):
    if not intervals:
        return 0, []

    # Step 1: Sort by start time, keep original index to map output later
    intervals = sorted([(start, end, i) for i, (start, end) in enumerate(intervals)])

    result = [0] * len(intervals)  # result[i] = room assigned to i-th meeting
    heap = []  # (end_time, room_number)
    next_room = 0  # room index counter
    available_rooms = []  # pool of reusable room numbers

    for start, end, idx in intervals:
        # Free up rooms that ended before this meeting starts
        while heap and heap[0][0] <= start:
            _, freed_room = heapq.heappop(heap)
            heapq.heappush(available_rooms, freed_room)

        # Assign room
        if available_rooms:
            room = heapq.heappop(available_rooms)
        else:
            room = next_room
            next_room += 1

        # Record assignment and push current meeting into heap
        result[idx] = room
        heapq.heappush(heap, (end, room))

    return next_room, result

intervals = [[0, 30], [5, 10], [15, 20]]
rooms_needed, assignments = assignMeetingRooms(intervals)

print("Rooms Needed:", rooms_needed)           # ➝ 2
print("Room Assignments:", assignments)        # ➝ [0, 1, 1] (for example)

"""
Input:
intervals = [[0, 30], [5, 10], [15, 20]]
Expected Output:
# Example: Each meeting assigned to a room number (can vary depending on order)
[
    (0, 30) → Room 0,
    (5, 10) → Room 1,
    (15, 20) → Room 1 (reuses Room 1 after it’s freed)
]
"""