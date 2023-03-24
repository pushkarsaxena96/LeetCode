from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (high + low)//2
           
            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                return int(mid)
            
        
        return low 


# Create an instance of the Solution class
solution = Solution()

# Call the search() method with the appropriate arguments
result = solution.searchInsert([1,3,5,6], 2)

# Print the result
print(result)