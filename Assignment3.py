
import random

class item:
    def __init__(self,k,v):
        self.key = k
        self.value = v
        self.next = None

class hashTable:
    def __init__(self, defCap, primer):
        self.defaultCapacity = defCap
        self.size = 0
        self.bucket = [None] * defCap
        self.a = random.randrange(primer)
        self.b = random.randrange(primer)
        self.p = primer
    
    def hash(self,str):
        #goal is to add a hash function that takes a string and returns an number
        max = (1 << 32) - 1 
        h = 0
        for char in str:
            # print(f"h << 5 is {h << 5}")
            # print(f"h >> 27 is {h >> 27}")
            h = ( h << 5 & max) | (h >> 27)
            h += ord(char)
        # print(h)
        return h

    def hashCompress(self,k):
        # using MAD
        # [(a+ bi)mod p]mod N
        # p is a prime number larger than N
        # a and b are random numbers from 0 to p - 1
        return (self.a + self.hash(k) * self.b) % self.p % len(self.bucket)

    def insert(self,val):
        exit
    
    def size(self):
        return len(self.bucket)
    
newHash = hashTable(256,12312313)
print(newHash.hashCompress("ziggy"))
print(newHash.hashCompress("edwin"))
print(newHash.hashCompress("cool"))

