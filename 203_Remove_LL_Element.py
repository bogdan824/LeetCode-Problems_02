class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next


ls = Node(1,None)
ls.next = Node(3,None)
ls.next.next = Node(2, None)
ls.next.next.next = Node(7, None)

def removeElements(self, head, val):
	dummy = ListNode(0)
	dummy.next = head
	previous = dummy
	current = head  
	while current is not None:
	    if current.val==val:
	        previous.next = current.next
	    else:
	        previous = current
	    current = current.next
	return dummy.next

removeElements(self, head, 6)
#1 Ceraate a dummy ListNode to ct as a previous of the head
#2 Assign dummy.next equals to head 
#3 Create a previous and a current node and assign it to dummy and head 
#                           					  (now we can navigate)
#4 Create a loop that iterates while current is not None
#5 If current.val == val then previous.next = current.next
#6                       else: previous = current
#7 curremt = current.next (o/s if else)
#8 Return dummy