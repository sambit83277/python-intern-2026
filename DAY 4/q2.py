# Count vowels in a string 
text = input()
count = 0
for ch in text:
    if 'A' <= ch <= 'Z':
        ch = chr(ord(ch) + 32)

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1
        
print("Vowel Count:", count)