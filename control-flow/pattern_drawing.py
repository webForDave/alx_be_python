size = int(input("Enter the size of the pattern: "))
number_of_rows = 0

if size:
    while number_of_rows != size:
        for i in range(size):
            print("*" * size)
            number_of_rows += 1
