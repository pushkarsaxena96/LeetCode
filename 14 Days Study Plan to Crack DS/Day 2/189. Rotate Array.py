from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Let the array be - 123456789 and k = 4

        Step 1 - 12345 6789 ---> 54321 6789

        Step 2 - 54321 6789 ---> 54321 9876

        Step 3 - 543219876 ---> 678912345
        
        """
        
        nums[:] = nums[-k%len(nums):] + nums[:-k%len(nums)]

        return nums
    
# Create an instance of the Solution class
solution = Solution()

# Call the search() method with the appropriate arguments
result = solution.rotate([1,2,3,4,5,6,7],3)

# Print the result
print(result)