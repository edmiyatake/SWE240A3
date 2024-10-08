SOME_RANDOM_NUMBER = 256

class Item:
    def __init__(self,k,v):
        self.key = k
        self.value = v
        self.next = None

class hashTable:
    def __init__(self):
        self.defaultCapacity = SOME_RANDOM_NUMBER
        self.size = 0
        self.bucket = [None] * self.defaultCapacity()
    
    def hashing(self):
        #goal is to add a hash function
        exit

    def insert(self,val):
        exit
    
    def size(self):
        return self.size
    
