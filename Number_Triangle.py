rows = int(input("Enter Total number of Rows: "))
number = 1

for n in range (1,rows + 1):
    for m in range (1,n + 1):
        print(number,end="")
        number += 1
    
    print()