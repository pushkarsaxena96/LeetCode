# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# Time o(n)
#Space Log(n)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        end = n
        start = 0 

        while start < end:
            mid = (start + end) // 2

            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start       