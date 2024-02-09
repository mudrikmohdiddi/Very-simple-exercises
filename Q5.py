"""5.	Write a function is_member() that takes a value (i.e. a number, string, etc)
x and a list of values a, and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the in operator does,
but for the sake of the exercise you should pretend Python did not have this operator.)"""

def is_member(x,a):
    for i in a:
        if(i==x):
            x=True
    if(x==True):
        return True
    else:
        return False
def main():
    print(is_member(11,[5,7,6,5,4,3,2,1]))
    print(is_member(6,[5,7,6,5,4,3,2,1]))
    print(is_member(19,[5,7,6,5,4,3,2,1]))
    print(is_member(1,[5,7,6,5,4,3,2,1]))
    print(is_member("i","mudrik"))
    print(is_member("p","mudrik"))

main()
