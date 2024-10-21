import random
import re

class item:
    def __init__(self,k,v):
        self.key = k
        self.val = v
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

    # later on, changed val to default none cause anagrams have no associted value yet
    def insert(self,key,val=None):
        newIndex = self.hashCompress(key)
        newItem = item(key,val)

        if not self.bucket[newIndex]:
            self.bucket[newIndex] = newItem
        else:
            curr = self.bucket[newIndex]
            while curr:
                # if key already exits, just update the value
                if curr.key == key:
                    curr.val = val
                    return
                if not curr.next:
                    curr.next = newItem
                    break
                curr = curr.next
        # always remember to update the size after inserts
        self.size += 1

    def getSize(self):
        return self.size
    
    def get(self,key):
        newIndex = self.hashCompress(key)
        curr = self.bucket[newIndex]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
    
    def printTable(self):
        for i, item in enumerate(self.bucket):
            print(f"Index {i}:", end=" ")
            curr = item
            while curr:
                print(f"({curr.key}, {curr.val})", end=" -> ")
                curr = curr.next
            print("None")

def countAnagram():
    newHash = hashTable(1000,7919)
    with open("pride-and-prejudice.txt",'r') as file:
        for line in file:
            words = re.split(r"[^a-zA-z0-9]",line)
            for word in words:
                anagram = ''.join(sorted(word.lower()))
                newHash.insert(anagram)

    return newHash.getSize()

# newHash = hashTable(256,12312313)
# print(newHash.hashCompress("ziggy"))
# print(newHash.hashCompress("edwin"))
# print(newHash.hashCompress("cool"))

# picked a random prime from wikipedia
# newMap = hashTable(100,7919)

# Insert test cases (key-value pairs)
# newMap.insert("apple", 100)
# newMap.insert("banana", 200)
# newMap.insert("grape", 300)
# newMap.insert("orange", 400)
# newMap.insert("melon", 500)

# newMap.getSize()
# newMap.printTable()
# print(countAnagram())