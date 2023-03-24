from math import ceil
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mapped = []
        n = 0
        while head:
            mapped.append(head)
            n += 1
            head = head.next
        k = n // 2 if n % 2 else ceil(n/2)
        return mapped[k]
    

# Create an instance of the Solution class
solution = Solution()

# Call the search() method with the appropriate arguments
result = solution.middleNode([1,2,3,4,5])

# Print the result
print(result)    
