import time

class Solution:
    def isValidUsingIf(self, s: str) -> bool:
        stack = []
        for item in s:
            print("existing stack:" + str(stack) )
            if  item in ['(', '{', '[']:
                stack.append(item)
            else:
                if not stack:
                    return False
                if item == ')' and stack[-1] == '(':
                    stack.pop()
                elif item == '}' and stack[-1] == '{':
                    stack.pop()
                elif item == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
                
            print("new stack:" + str(stack) )    
        return not stack
    
    def isValidUsingMatchHash(self, s: str) -> bool:
        stack = []
        match = {"(": ")", "[": "]", "{": "}"}
        for item in s:
            if item in ')]}':
                if len(stack) == 0 or match[stack[-1]] != item:
                    return False
                stack.pop()
            else:
                stack.append(item)

        return len(stack) == 0             


solution = Solution()

start_time = time.time()



result = solution.isValidUsingIf("{[]}")
# Print the result
print(result)     

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
