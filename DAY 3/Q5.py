#REVERSE THE STRING
x=input("enter the string:")
rev1=x[::-1]
print("reverse by slicing:",rev1)
rev2=""
for i in x:
    rev2 = i + rev2
print("reverse by loop:",rev2)