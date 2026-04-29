SP = float(input("Please Enter Selling Price: "))
CP = float(input("Please Enter Cost Price: "))

if SP > CP:
    profit = SP - CP
    print("Total Profit = ",(profit))

else:
    CP < SP
    loss = CP - SP
    print("Total Loss = ",(loss)) 