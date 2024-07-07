pattenSize = int(input("Enter the size of the pattern: "))
row = 1
while row <= pattenSize:
    for _ in range(pattenSize):
        #It means that you do not need a variable to hold the current value from the range; you just want to repeat the loop body based on patternSize number of time
        print("*", end=" ")
    print()
    row += 1
    