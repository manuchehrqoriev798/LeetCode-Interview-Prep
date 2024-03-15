from random import randint
 
class RandomizedSet(object):
 
    def __init__(self):
        # Key is the string, value is the index of the string inside the array
        # Use this hashmap to keep track of the position of the string in the array
        self.item_to_index = {}
        
        # The array of strings we have inserted
        self.item_arr = []
 
    def insert(self, item):
        # Only insert if the string does not already exist
        if item in self.item_to_index:
            return False
        
        # Append this new string to the end of the array
        index = len(self.item_arr)
        self.item_to_index[item] = index
        self.item_arr.append(item)
 
        return True
        
    def remove(self, item):
        # Only remove if the string exists
        if item not in self.item_to_index:
            return False
        
        # Swap the string to be removed to the end of the array
        index = self.item_to_index[item]
        last_item = self.item_arr[-1]
        self.item_to_index[last_item] = index
        self.item_arr[index] = last_item
        self.item_arr.pop()
        del self.item_to_index[item]
        
        return True
 
    def getRandom(self):
        # Randomly pick an index available
        index = randint(0, len(self.item_arr) - 1)
        return self.item_arr[index]