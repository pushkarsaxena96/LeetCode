from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       
        # Solution 1
        # for i in range(nums.count(0)):
        #     nums.remove(0)
        #     nums.append(0) 

        # Solution 2

        j = 0
        for i in range(len(nums)):            
            if nums[i] != 0 and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]

            # wait while we find a non-zero element to
            # swap with you
            if nums[j] != 0:
                j += 1
        
        print("Final: " + str(nums))
        
    

# Create an instance of the Solution class
solution = Solution()

# Call the search() method with the appropriate arguments
result = solution.moveZeroes([0,1,0,3,12])

# Print the result
print(result)