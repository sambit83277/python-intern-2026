#CHECK IF STRING IS PALINDROME OR NOT
a=input("enter the string:")
rev=a[::-1]
if a==rev:
    print("palindrome")
else:
    print("not palindrome")