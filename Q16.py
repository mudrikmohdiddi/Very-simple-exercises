"""16.	Write a function filter_long_words() that takes a list of words and an integer n and
returns the list of words that are longer than n."""

def filter_long_words(word,integer):
    long_word=[]
    for i in word:
        if(len(i)>integer):
            long_word.append(i)
    return long_word

def main():
    print(filter_long_words(["mudrik","mohd","iddi","mulhat","sabraa","neema","nasma","mmanga"],5))
main()
