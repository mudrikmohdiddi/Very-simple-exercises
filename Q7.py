"""7.	Define a procedure histogram() that takes a list of integers and
prints a histogram to the screen. For example,histogram([4, 9, 7]) should print the following:
**** ********* ******* """

def histogram(list):
    for a in list:
        for b in range(a):
            print("*",end=" ")
        print()

def main():
    histogram([4,9,7,10,3,4,8])
main()


            
    
