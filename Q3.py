"""3.	Define a function sum() and a function multiply() that sums and multiplies
(respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24."""

def sum(list):
    sum=0
    for i in list:
        sum+=i
    return f"Sum of list {list} is {sum}"

def multiply(list):
    multiply=1
    for i in list:
        multiply*=i
    return f"Multiply of list {list} is {multiply}"  

def main():
    print(sum([1,2,3,4]))
    print(multiply([1,2,3,4]))
main()
