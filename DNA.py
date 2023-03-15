#  File: DNA.py

#  Description:

#  Student Name: Anika Srivastava

#  Student UT EID: as86323

#  Partner Name: Melani Rodriguez

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 8-26

#  Date Last Modified: 8-28

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.
import sys


# takes a single string and returns a list of all the substrings of that string

def all_substrings(s):
# creates an empty list that will hold the common subsequences
    result = []

    # define the size of the window
    wnd = len(s)

    # generate all substrings
    while (wnd > 0):
        index = 0
        while(index + wnd) <= len (s):
            # get the substring
            sub_string = s[index:index + wnd]
            result.append(sub_string)
            index += 1
        #decrease the size of the window
        wnd = wnd - 1

    #return the result
        return result

# take two strings and return a list of the longest common subsequence between the two strings, if there is no common substring, you get an empty list
def longest_subsequence(s1, s2):
    longest_sub = "" 
    
    while len(s1) <= 80 and len(s2) <= 80:
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if(s1[i] == s2[j]):
                    longest_sub += s1[i]
        return(longest_sub)


def test_cases():
    # test the function longest_subsequence - using assert function
    assert longest_subsequence ("a", "a") == ["a"]
    assert longest_subsequence ("abcd", "bc") == ["bc"]
    assert longest_subsequence ("abcd", "xyz") == []
    assert longest_subsequence ("abcde", "abcd") == ["abcd"]
    assert longest_subsequence ("abc", "ac") == ["a"]

    # test the function all_substrings
    assert all_substrings ("a") == ["a"]
    assert all_substrings ("abc") == ["a", "b", "c", "ab", "bc", "abc"]
    
    # other test cases

    # return the result
    return "all test cases passed"

def main():

    # call test_cases()
    print(test_cases())
    
    # read the number of pairs
    num_pairs = sys.stdin.readline()
    
    # strip function removes end spaces and beginning spaces
    num_pairs = num_pairs.strip()
    num_pairs = int(num_pairs)
    
    # use find command in checking whether the shortest string is in the longest string - problem is about finding substrings within a string!!
    
    print (num_pairs)

    # for each pair find the common sequence
    for i in range (num_pairs):
        st1 = sys.stdin.readline()
        st2 = sys.stdin.readline()
        
        st1 = st1.strip()
        st2 = st2.strip()
        
        st1.upper()
        st2.upper()
    
        print(st1)
        print(st2)
        
        # get the longest subsequences
        long_sub = longest_subsequence (st1, st2)
        
        # print the result
        # print("The longest common subsequence between " + st1 + " and " + st2 + " is: " + long_sub)
        
if __name__ == "__main__":
# if there is a function called main, run the function
    main()
