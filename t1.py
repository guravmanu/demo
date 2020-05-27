def ispalindromestr(s):
    str1=str[::-1]
    if str==str1:
        print("given string is plindrome")
        print("orignal string ",str,"","reverse string ", str1)
    else:
         print("string is not palindrome")
a=1
while a==1:
    str=input("enter a string")
    ispalindromestr(str)
    a= int(input("enter 1 for continue 0 for stop"))
