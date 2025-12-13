import math
x1 = int(input("enter x1  :- "))
y1 = int(input("enter y2 :- "))

x2 = int(input("enter x2 :- "))
y2 = int(input("enter y2 :- "))

distance = math.sqrt((x2-x1**2 + (y1-y2)**2))
print(f"{distance :.3f}")


