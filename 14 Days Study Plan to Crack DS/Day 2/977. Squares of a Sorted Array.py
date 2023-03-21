from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left, right, = 0, n - 1
        index = n - 1
        result = [0 for x in nums]

        while index >= 0:

            if (abs(nums[left]) > abs(nums[right])):
                result[index] = nums[left] * nums[left]
                left = left + 1
            else:
                result[index] = nums[right] * nums[right]
                right = right - 1

            print(result)    

            index = index - 1

        return (result) 
    
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        return nums 
    

# Create an instance of the Solution class
solution = Solution()

# Call the search() method with the appropriate arguments
result = solution.sortedSquares([-4,-1,0,3,10])

# Print the result
print(result)