#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    
    for i in range(0, len(weights)): # for i in range of 0 and the length of the weights.
        
        wt = weights[i] # Set wt to weights[i]
         
        retrieve = hash_table_retrieve(ht, limit - wt) # set retrieve to hash table retrieve `limit - weight`
        
        if retrieve is None:
            hash_table_insert(ht, wt, i) # then return hash table insert
            print(f'Weight Index: {i} Value: {wt}')
        
        else:
            return (i, retrieve) # return i, and retrieve
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
