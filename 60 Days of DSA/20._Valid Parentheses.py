import time

"""
    Findings : 
    1. Double pass Has is the fastest
    2. Single pass List may become slow in case of big list of input
    3. Single pass has an extra iteration
"""

class Solution:
    def isValid(self, s: str) -> bool:
        hashTable = {'(' : 0, ')' : 1, '{' : 2, '}' : 3, '[' : 4, ']' : 5}
        for i in range(0,len(s),2):
            print("iteration:" + str(i))
            print(hashTable[s[i]] % 2)
            print(hashTable[s[i+1]] % 2)

            if hashTable[s[i]] % 2 == 0 & hashTable[s[i+1]] % 2 != 0 :
                pass
            else:
                return False
        return True         


solution = Solution()

start_time = time.time()



result = solution.isValid("()[[{}")
# Print the result
print(result)     

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
