Medical_Cause = input("Did you have any Medical cause? Y/N: ").strip().upper()

if Medical_Cause=='Y':
    print("Allowed")

else:
    Attendence = int(input("Enter the Attendence: "))
    if Attendence >=75:
        print("Allowed")
    else: 
        print("Not allowed")
