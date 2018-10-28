class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


        
def mergeSort(head):
    if(head is None or head.next is None):
        return head
    
    a = head
    b = head.next
    while(b is not None and b.next is not None):
        a = a.next
        b = b.next.next
    left = head
    right = a.next
    
    a.next = None
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    if(left is None):
        return right
    if(right is None):
        return left
    
    head = None
    if(left.val < right.val):
        head = left
        left = left.next
    else:
        head = right
        right = right.next
    
    temp = head
    while(right is not None and left is not None):
        if(left.val < right.val):
            temp.next = left
            left = left.next
            temp = temp.next
        else:
            temp.next = right
            right = right.next
            temp = temp.next
    
    if(right is not None):
        temp.next = right
    if(left is not None):
        temp.next = left

    return head
    


a = ListNode(1)
a.next = ListNode(5)
a.next.next = ListNode(4)
a.next.next.next = ListNode(3)

a = mergeSort(a)

iterator = a
while(iterator is not None):
    print(iterator.val)
    iterator = iterator.next