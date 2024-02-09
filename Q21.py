"""21.	Write a function char_freq() that takes a string and
builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary.
Try it with something likechar_freq("abbabcbdbabdbdbabababcbcbab")."""

def char_freq(string):
    letter=list(set(string))
    frequency=[]
    sum=0
    for a in letter:
        sum=0
        for b in string:
            if(a in b):
                sum+=1
                
        frequency.append(f"{a}:{sum}")
    print(frequency)
def main():    
    char_freq("abbabcbdbabdbdbabababcbcbab")
main()
