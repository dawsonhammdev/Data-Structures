"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        # it's going to basically equal the node to be none.
        # we are making the second node in the list equal to what the current head.prev is which is None
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # 'value' is not a node so we need to create it.
        new_node = ListNode(value)
        # increment the length by 1
        self.length += 1
        # need to make sure we add to the head correctly when the linked list is completely empty
        # if the list is empty we need to point the head and the tail to the 'new_node'
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # the list already has elements in it:
            # we want to point the current head to the new_node and have the new_node point to the old head.
            # point new_node to current head
            new_node.next = self.head
            # point current head prev to the new_node
            self.head.prev = new_node
            # point head to the new node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
        

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        # if the list is empty then do nothing
        if not self.head and not self.tail:
            return
        # if there is only one element in the list. 
        if self.head == self.tail:
            # We need to set the tail and head to none to delete the entire list.
            self.head = None
            self.tail = None
        # if the node we want to delete is the head
        elif self.head == node:
            # update the head to point to the node the current head was pointing to next.
            self.head = node.next
            # make the old head equal None by calling on the delete() function
            node.delete()
        # if the node we want to delete is the tail
        elif self.tail == node:
            # update the tail to point to the node the current tail was pointing to prev.
            self.tail = node.prev
            node.delete()
        # if the node is just some node in the list:
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # if the highest value is not the head:
        if not self.head:
            # return None
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val
