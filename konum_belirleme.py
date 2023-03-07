sayix= int(input("X değerini belirle ="))
sayiy= int(input("Y değerini belirle ="))

for i in range (sayix):
    if i==0:
        print(" "+"X", end="")
    else:
        print("X", end="")
        if i==sayix-1:
            print()
for j in range (sayiy):
    if j==sayiy-1:
        print("|"+" "*(sayix-1)+"X")
    else:
        print("|")