"""1.	Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in,
but writing it yourself is nevertheless a good exercise.)"""

def length(str_list):
    if("," in str_list):
        list=str_list.split(",")
        sum=0
        for i in list:
            sum+=1
        return f"Lengthe of list={sum}"
    else:
        sum=0
        for i in str_list:
            sum+=1
        return f"Lengthe of string={sum}"
def main():
    while(1==1):
        str_list=input("Please enter list or strig but not both:")
        str_list=str_list.removeprefix("[")
        str_list=str_list.removesuffix("]")
        print(length(str_list))
main()
        
