def reverse_ll(ll):
    """
    Receive a LinkedList as an input and return a reversed order LL

    Steps: 
    1. Each node needs to point to the previous node
    2. Head and tail pointers need to be flipped

    Cases:
    1. If the LL is empty, return the original that is pass in
        

    reverse_ll(LinkedList())
    return the empty list


    """
    # # If LL is empty, return LL
    # if ll.head is None:
    #     return ll
    
    # # If LL has one node
    # if ll.head is ll.tail:
    #     return ll

    # If LL has more than one node
    current = ll.head
    previous = None
    next_node = None
    while current is not None:
        # store a pointer to the current next_value
        # This has to happen before current.set_next(previous) so that we keep "Sean" a connection to "Sean" and "Beej" from the example
        next_node = current.get_next()

        # switch current's next pointer to the previous
        current.set_next(previous)

        # increment logic
        previous = current
        current = next_node

    ll.head, ll.tail = ll.tail, ll.head