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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the value to the root's value to determine which direction
        # if the value < root's value 
        # self.value is referring to the root.
        if value < self.value:
            # go left 
            # how do we go left?
            # check to see if the left side of the root is empty
            if self.left is None: 
                # then self.left is a Node 
                # now what?
                # insert the value there.
                self.left = BSTNode(value)
            else:
                # call the insert method on the child node to run the logic for us.
                self.left.insert(value)
        if value >= self.value:
                
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # test the root to see if it is the value
        if self.value == target:
            return True
        # testing if the root is less than the target value
        if target < self.value:
            # if the target is less but still not the target then return false
            if not self.left:
                return False
            # but if it is we need to recursively call the contains function on the parent and return back up the tree true.
            else:
                return self.left.contains(target)
        # if the the target is greater
        else:
            #we go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high 
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
