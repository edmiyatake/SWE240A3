# UCI SWE240 Assignment 3 Edwin Miyatake 61346496

Task Description: Complete the following task.

Task-1: Implement a Hash data structure from scratch. You can’t use built-in Hash or Dictionary APIs. You can use a built-in Array or List or your custom-built LinkedList.  The Hash class must have the following functions and fields - 

HashTable: A fixed-size array or list. Depending on your hash function, this array or list can be one-dimensional or two-dimensional. 
hash(x): A hash function that converts a string x to an integer, i.e., index in the hashtable. You can implement any hash function described in the textbook. Your hash function must have a collision-resolution mechanism.
insert(x):  Insert string x to the HashTable in the index returned by hash(x).
size():  Returns the size of the elements, i.e., the number of keys.
Write sample test cases to validate your implementation.

Task-2: Read and parse each word from the file pride-and-prejudice.txt Download pride-and-prejudice.txt. Note that this file is very large; therefore, reading the text at once will crash your program. You should read the text line by line. To split a line into words, you can consider anything other than alpha-numeric (i.e. [a-zA-Z0-9]) characters as delimiters, for example, ‘\n’, ‘\t’, ‘,’, ‘.’ etc. 

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, `mango` and `gonma` are anagrams containing the same characters. Write a function that would find out how many unique anagram-root words are there in the novel. An anagram-root word is a word that is derived by sorting the word by characters. For example, `mango`’s anagram root is `agmno`. 

To find the number of unique anagram roots, do the following steps.

Step-1: While you parse each word from the file, sort the words by character. You can use any built-in sorting API. 
Step-2: Insert the sorted words in the hashtable you implemented above. If the word is already present in the hashtable, then skip it. 
Step-3: Once all the words have been sorted and inserted (or skipped), call the size() function of the Hash class.
 
