"""2.	Write a function that takes a character (i.e. a string of length 1)
and returns True if it is a vowel, False otherwise."""

def vowel(character):
    vowel=["a","e","i","o","u"]
    if(character in vowel):
        return True
    else:
        return False

def main():
    while(9==9):
        character=input("Please enter character to check is vowel:")
        print(vowel(character.lower()))
main()
