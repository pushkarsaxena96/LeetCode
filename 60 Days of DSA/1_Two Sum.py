import time

"""
    Findings : 
    1. Double pass Has is the fastest
    2. Single pass List may become slow in case of big list of input
    3. Single pass has an extra iteration
"""

class Solution(object):
    def twoSumWithDoublePassHash(self, nums, target):
        numMap = {}
        n = len(nums)
        
        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        print(numMap)

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        
        return []  # No solution found      
    

    def twoSumWithSinglePassHash(self, nums, target):
        numMap = {}
        n = len(nums)
        
        # Find the complement
        for i in range(n):
            print("iteration:" + str(i))
            print("Old:" + str(numMap))
            complement = target - nums[i]
            print(complement)
            if complement in numMap:
                return [i, numMap[complement]]
            numMap[nums[i]] = i
            print("New:" + str(numMap))
        
        return []  # No solution found     


    def twoSumWithDoublePassList(self, nums, target):
        n = len(nums)
        
        # Find the complement
        for i in range(n):
            print("iteration" + str(i))
            complement = target - nums[i]
            if complement in nums:
                return [i, nums.index(complement)]
        
        return []  # No solution found     


solution = Solution()

start_time = time.time()

result = solution.twoSumWithDoublePassHash([2,7,11,15], 9)
#result = solution.twoSumWithDoublePassList([2,7,11,15], 18)
#result = solution.twoSumWithSinglePassHash([2,7,11,15], 18)



# Print the result
print(result)     

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
