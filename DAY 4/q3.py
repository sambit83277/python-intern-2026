x=input("enter the string:")
temp=0
for i in x:
    if (ord(i)>=48 and ord(i)<=57) or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
       temp=1
    else:
        temp=0
        break
if temp==1:
    print("all charecter is alphanumeric")
else:
    print("all charecter is not alphanumeric")