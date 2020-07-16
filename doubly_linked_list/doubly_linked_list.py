"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.previous = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    ### RUNS
    def add_to_head(self, value):
        # create an instance of ListNode with value
        new_node = ListNode(value)
        
        # if DLL is empty
        if self.length == 0:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        
        # if DLL is not empty
        else:
            # set new node's next to current head
            new_node.next = self.head
            # set head's prev to new node
            self.head.prev = new_node
            # set head to the new node 
            self.head = new_node
            
        # increment the DLL length attribute
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        currentHead = self.head

        # delete the head
        # if head.next is not None
        if self.head.next is not None:
            # set head.next's prev to self's None
            self.head.next.prev = None
            # set head to head.next
            self.head = currentHead.next
        # else (if head.next is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
        # decrement the length of the DLL
        self.length -= 1
        # return the value
        return currentHead.value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create an instance of ListNode with value
        new_node = ListNode(value)

        # if DLL is empty
        if self.length == 0:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tails's next to new node
            self.tail.next = new_node
            # set tail to the new node 
            self.tail = new_node
        
        # increment the DLL length attribute
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        currentTail = self.tail

        
        # delete the tail
        # if tail.prev is not None
        if self.tail.prev is not None:
            # set tail.prev's next to None
            self.tail.prev = None
            # set tail to tail.prev
            self.tail = currentTail.prev
        # else (if tail.prev is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None

        # decrement the length of the DLL
        self.length -= 1
        # return the value
        return currentTail.value
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        else:
            self.delete(node)
            self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        else:
            self.delete(node)
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Is the list empty? Then do nothing.
        
        if not node:
            return

        # If there is one node
        elif self.length == 1:
            self.head = None
            self.tail = None

        # If the node you're deleting is the head
        elif node is self.head:
            self.head = node.next

        # If the node you're deleting is the tail
        elif node is self.tail:
            self.tail = node.prev 

        # If it's somewhere else
        else:
            node.delete()
            
        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # start at the head
        currentVal = self.head
        highestVal = self.head.value
        # set the condition or set to the tail
        while currentVal.next is not None:
            currentVal = currentVal.next
            if currentVal.value > highestVal:
                highestVal = currentVal.value
        return highestVal

# dll = DoublyLinkedList(1)
# dll.add_to_tail(3)
# dll.add_to_tail(5)
# dll.add_to_tail(6)
# dll.get_max()