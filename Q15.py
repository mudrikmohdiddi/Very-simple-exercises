"""15.	Write a function find_longest_word()
that takes a list of words and returns the length of the longest one."""

def longest_word(word):
    longest=0
    long_word=""
    for i in word:
        if(len(i)>longest):
            longest=len(i)
            long_word=i
    return long_word
def main():
    print(longest_word(["mudrik","mohd","iddi","mulhat","sabraa","neema"]))
main()
        
