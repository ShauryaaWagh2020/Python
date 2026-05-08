num = int(input("Enter the number: "))
original = num
count = 0 

while num > 0:
    num //= 10
    count += 1

print(original,"has total",count,"digits.")