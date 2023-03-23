from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        
       return " ".join([w[::-1] for w in s.split(" ")])
        
    

# Create an instance of the Solution class
solution = Solution()

# Call the search() method with the appropriate arguments
result = solution.reverseWords("Let's take LeetCode contest")

# Print the result
print(result)