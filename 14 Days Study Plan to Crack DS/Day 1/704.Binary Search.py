from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums)-1
        mid = 0

        while low<=high:
            mid = (high + low)//2

            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                return int(mid)
            
        
        return -1


# Create an instance of the Solution class
solution = Solution()

# Call the search() method with the appropriate arguments
result = solution.search([-1,0,3,5,9,12], 13)

# Print the result
print(result)