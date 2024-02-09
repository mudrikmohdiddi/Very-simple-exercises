"""4.	Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I"."""

def reverse(string):
    new=""
    for i in range(len(string)-1,-1,-1):
        new+=string[i]
    return new

def main():
    string=input("Please enter string:")
    print(reverse(string))
main()
        
