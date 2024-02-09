"""13.	Write a function max_in_list() that takes a list of numbers and returns the largest one."""

def max_in_list(list_number):
    large=list_number[0]
    for i in list_number:
        if(i>large):
            large=i
    print(large)

def main():
    max_in_list([3,2,9,12,6,7])
main()
    
        
