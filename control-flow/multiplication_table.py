number = int(input("Enter a number to see its multiplication table: "))

if number: 
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")