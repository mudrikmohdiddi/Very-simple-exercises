"""14.	Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words."""

def word_integer(list):
    integer=[]
    for i in list:
        integer.append(len(i))
    return integer
def main():
    print(word_integer(["mudrik","mohd","iddi","mmanga","neema","sabraa","haitham","mulhat"]))
main()
