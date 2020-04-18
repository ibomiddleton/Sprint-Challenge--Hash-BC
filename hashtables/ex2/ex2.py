#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    
    for i in tickets: # for i in tickets, insert the hashtable, source and the destination
        print(i.source)
        print(i.destination)
        
        hash_table_insert(hashtable, i.source, i.destination) # hash table insert function ht, source, and destination
    
    destination = hash_table_retrieve(hashtable, 'NONE') # account for NONE
    
    while destination is not 'None':
        
        route.append(destination) # append destination to route
        
        destination = hash_table_retrieve(hashtable, destination) # destination set to retrieve ht, destination
        
    return route