pattenSize = int(input("Enter the size of the pattern: "))
row = 1
while row <= pattenSize:
    for _ in range(pattenSize):
        print("*", end=" ")
    print()
    row += 1
    