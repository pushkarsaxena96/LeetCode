from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s
            
        
    

# Create an instance of the Solution class
solution = Solution()

# Call the search() method with the appropriate arguments
result = solution.reverseString(["h","e","l","l","o"])

# Print the result
print(result)