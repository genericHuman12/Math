x= int(input("Pick a number:"))
y = int(input("Pick Another:"))
c = 1
bob = []
while not c == 0:
    if x > y:
        c = x//y
        bob.append(c)
    elif y > x:
        c=y//x
        bob.append(c)
    if list[-1] == 0:
        print(list[-2])