"""18.	A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a pangram or not."""

def pangram(sentance):
    sum=0
    list_letter=[]
    for i in sentance:
        if(i.isalpha()):
            list_letter.append(i.lower())
    for i in set(list_letter):
        sum+=1
    if(sum==26):
        return "The sentance pangram"
    else:
        return "The sentace is not pangram"

def main():
    while(2==2):
        sentance=input("Please enter sentance:")
        print(pangram(sentance))
main()
            
