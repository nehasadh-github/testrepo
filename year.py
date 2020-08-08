"""9)	Write a function that’s check if the string passed is palindrome or not.
Example:-
Input string=”DaD”
After reverse DaD so its palindrome
	
Input=”Hello”
Reverse is “olleH” as both not equal so not pallindrome
"""
def palindrome(a):
    b=""
    for i in a:
        b=i+b
    if(a==b):
        print("its palindrome")
    else:
        print("its not palindrome")

string=input("enter string::")
palindrome(string)