print("Grade 10 enrolment \n")

age = int(input("Enter your Age: "))

if age <=20:
    if age >=10:
        print("Enrolment Successful!: Student's age met the requirement for grade 10.")
    else:
        print("Enrolment Failed :Student is younger than required age range (Under 10).")

else:
    print("Enrolment denied: Student is older than required age range (Above 20).") 