import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()                    #Blank Linked List

        while list1 and list2:                      #Looping through the Entered LinkedLists
            if list1.val < list2.val:
                print("while=if")
                print(list1.val)
                print(list2.val)
                cur.next = list1                    #Smaller value's reference is set for Cur.Next i.e. Blank Linked List's next value
                list1 = list1.next                  #Incrementing List 1
                print(cur.val)
            else:
                print("while-else")
                print(list1.val)
                print(list2.val)
                cur.next = list2                    #Smaller value's reference is set for Cur.Next i.e. Blank Linked List's next value
                list2 = list2.next                  #Incrementing List 2
                print(cur.val)
            cur = cur.next
        
        cur.next = list1 if list1 else list2        #Check for blank Lists
        
        return dummy.next                           #Return Elements after head() of Dummy

solution = Solution()
start_time = time.time()

# Create ListNode objects for list1 and list2
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

result = solution.mergeTwoLists(list1, list2)

# Traverse the resulting linked list and print its values
while result:
    print(result.val, end=" ")
    result = result.next

end_time = time.time()
execution_time = end_time - start_time
print("\nExecution time:", execution_time, "seconds")