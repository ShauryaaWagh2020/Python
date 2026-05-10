num = int(input("Enter the decimal number : "))
binary = ""

while num > 0:
    remainder = num & 2
    binary = str(remainder) + binary
    num //= 2

    print ("Binary number is : ",binary)
