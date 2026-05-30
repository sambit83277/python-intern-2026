# First Non-Repeating Character
s = input()

found = False

for ch in s:
    count = 0

    for c in s:
        if c == ch:
            count += 1

    if count == 1:
        print("First Non-Repeating Character:", ch)
        found = True
        break

if not found:
    print("No non-repeating character found")