
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        add_value = self.storage.append(value)
        self.size = self.size + 1
        return add_value

    def dequeue(self):
        if self.size > 0:
            remove_value = self.storage.pop(0)
            self.size = self.size - 1
            return remove_value
        else:
            print("Nothing here")

class Stack:
    def __init__(self, ):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.size = self.size + 1
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            print("Sorry, nothing here!")
            return 
        else:
            popped = self.storage.pop(self.size - 1)
            self.size = self.size - 1
            return popped

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        pass
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # Else 
            else:
                # Repeat the process on left subtree
                self.left.insert(value)
        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # if there is no right childe, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # repeat the process on right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.right.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check is self.right is None
        # if self.right is None, return self.value
        # else self.right.get_max(self)

        if not self:
            return None

        """ recursive """
        if self.right:
            return self.right.get_max()
        return self.value

        """ iterative """
        # initialize max_value variable; this will be updated as we traverse the tree
        # max_value = self.value
        #get a reference to the node we're currently at; update this value
        # current = self
        # check to see if we're still at a valid tree node
        # while current:
            # if current value is greater than max_value, update the max_value
            # if current.value > max_value:
            #     max_value = current.value
            # move on to the next right node in the tree
        #     current = current.right
        # return max_value

        # if self.value == None:
        #     return self.value
        # else:
        #     return self.get_max(self.right)
            
        # print(type(self.value))
        # print(type(self.right))
        # if self.value is not None:
        #     if self.value < self.right:
        #         return self.right.get_max()
        #     else: 
        #         return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
        

    # Part 2 -----------------------

    # """preorder"""
    # visit logic
    # print(self.value)
    #recurse left
    # self.left.fn()
    #recurse right
    # self.right.fn()

    # """inorder"""
    # visit logic
    #recurse left
    # self.left.fn()
    # visit logic
    # print(self.value)
    #recurse right
    # self.right.fn()

    # """postorder"""
    # visit logic
    #recurse left
    # self.left.fn()
    #recurse right
    # self.right.fn()
    # visit logic
    # print(self.value)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return 

        # check if we can move left
        # if self.left is not None:
        if self.left is not None:
            self.left.in_order_print(self.left)

        # visit the self by printing its value
        print(self.value)

        # check if we can move right
        if self.right is not None:
            self.right.in_order_print(self.right)
        

        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        """FIFO - first in first out (line image)"""
        # use a queue to form a "line"
        queue = Queue()
        # for the nodes to "get in"

        # start by placing the root in the queue
        queue.enqueue(node)
        
        # need a while loop to iterate
        # while length of queue is greater than 0
        while queue.__len__() > 0:
            val = queue.storage[0]
            if val.left is not None:
                # place current item's left node in queue if not None
                queue.enqueue(val.left)
            if val.right is not None:
                # place current item's right node in queue if not None
                queue.enqueue(val.right)
            # print that item
            queue.dequeue()
            print(val.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize an empty stack
        stack = Stack()
        # push the root node onto the stack
        if node is not None:
            stack.push(node)

        # need a while loop to manage our iteration
        # if stack is not empty start the while loop
        while stack.__len__() > 0:
            val = stack.storage[-1]
            stack.pop()
            if val.right is not None:
                stack.push(val.right)
            if val.left is not None:
                stack.push(val.left)
            print(val.value)
            # pop top item off the stack
            # print that item's value

            # if there is a left subtree
                # push left item onto the stack

            # if there is a right subtree
                # push right item onto the stack
                # prints the last one first LIFO - last in first out (pringles can image)
    def __str__(self):
        return f"\n {self.value}, {self.left}, {self.right}"

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        """ ROOT --> LEFT --> RIGHT """
        if self is None:
            return 
        
        print(self.value)

        if self.left is not None:
            self.left.pre_order_dft(node)

        if self.right is not None:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        """ LEFT --> RIGHT --> ROOT"""

        if self is None:
            return 
        
        if self.left is not None:
            self.left.post_order_dft(node)

        if self.right is not None:
            self.right.post_order_dft(node)
        
        print(self.value)

# test = BSTNode(1)
# test.insert(5)
# test.insert(2)
# test.insert(3)
# test.insert(7)
# test.insert(6)
# print(test)