class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create a list of list of strings called result
        result = {}

        # for all words in strs
        for word in strs:
            count = [0]*26 # a ... z

            # get the ascii value of each word
            for character in word:
                count[ord(character) - ord("a")] += 1

            # because lists cannot be keys for maps, make it a tuple
            # NOTES:
            #       (1) Immutability: Tuples are immutable, meaning their elements cannot be changed after creation. 
            #           This immutability makes them suitable for use as dictionary keys. Since the character count 
            #           for each group of anagrams should remain constant throughout the program's execution, using a 
            #           tuple as the key ensures that the key won't change accidentally.
            #       (2) Hashability: Tuples are hashable, which means they can be used as keys in dictionaries 
            #           (including defaultdicts). Dictionaries use hash values of keys for efficient lookup and retrieval.
            #           Since tuples are hashable, they can serve as reliable keys to access values in the result dictionary 
            #           efficiently.
            #       (3) Uniqueness: Tuples are unique based on their elements' order and values. In this code, the character 
            #           count of letters in each word uniquely identifies a group of anagrams. By converting the list count to a tuple, 
            #           you create a unique representation of that character count, allowing you to group anagrams with the same character 
            #           count together.
            #       (4) Comparison: Tuples support comparison operations, which is important for dictionary keys. This enables
            #           the code to identify whether two character count tuples are the same or different.
            count_tuple = tuple(count)
            
            # now check if the map contains the key or not and either (1) append or (2) create a new key
            if count_tuple in result:
                result[tuple(count_tuple)].append(word)
            else:
                result[tuple(count_tuple)] = [word]

        return result.values()