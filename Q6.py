"""6.	Define a function overlapping() that takes two lists and
returns True if they have at least one member in common, False otherwise.
You may use your is_member() function, or the in operator,
but for the sake of the exercise, you should (also) write it using two nested for-loops."""

def overlapping(list_one,list_two):
    common=False
    for a in list_one:
        for b in list_two:
            if(a==b):
                common=True
    if(common==True):
        return True
    else:
        return False
def main():
    print(overlapping([1,2,3,4],[9,8,7,6,5]))
    print(overlapping([1,2,9,3,4,5,6],[9,8,7,6,5]))
    print(overlapping(["mudrik","ali","said"],["fatma","ali","khadija"]))
    print(overlapping(["mudrik","ali","said"],["fatma","khadija"]))

main()
        
        
