class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        hour %= 12

        minangle = 6*minutes
        hourangle = 30*hour + 0.5*minutes

        diff = abs(hourangle-minangle)

        return min(diff, 360-diff)