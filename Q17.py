"""17.	Write a version of a palindrome recognizer that also
accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?",
"Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!". Note
that punctuation, capitalization,
and spacing are usually ignored."""

def palindrome(word):
    og=""
    reverce=""
    for i in word:
        if(i.isalpha()):
            og+=i.lower()
    for i in range(len(og)-1,-1,-1):
        reverce+=og[i]
    if(og==reverce):
        return "Palindrome"
    else:
        return "Not palindrome"
def main():
    while("d"=="d"):
        word=input("Enter sentance:")
        print(palindrome(word))
main()
        

