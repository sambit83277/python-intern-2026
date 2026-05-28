#CHECKING VALIDITY
password="github123"
username="git"
p=input("enter the password:")
u=input("enter the username:")
if p==password and u==username:
    print("login successful")
elif p==password:
    print("invalid username")
elif u==username:
    print("invalid password")
else:
    print("ERROR IN SIGNING IN")