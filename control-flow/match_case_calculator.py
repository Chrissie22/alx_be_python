number = int(input("Enter a number to see its multiplication table: "))
i = 1
for iterator in range(1, 10):
    if i <= 10:
        product = number * iterator
        i = i + 1
        print(f"{number} * {iterator} = {product}")
    
    