size = int(input("Enter the size of the pattern: "))
number_of_rows = 1

while number_of_rows <= size:
    for _ in range(size):
        print("*", end="")
    print("")
    number_of_rows += 1