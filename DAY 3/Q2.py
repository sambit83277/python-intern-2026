#CHARACTER AND LARGEST
x=input("enter string:")
largest=0
character='a'
for i in range(len(x)):
    count=0
    for j in range(len(x)):
        if x[i]==x[j]:
            count += 1
    if count>=largest:
        largest=count
        character=x[i]
print("character:",character)
print("count:",largest)