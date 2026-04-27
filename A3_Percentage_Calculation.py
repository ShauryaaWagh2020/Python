print("Enter Marks obtained in 4 Subjects:")

Math= int(input("Math:"))
Science= int(input("Science:"))
English= int(input("English:"))
Hindi= int(input("Hindi:"))

sum= (Math + Science + English + Hindi)
print("The sum of Math,Science,English,Hindi:",sum)

perc= (sum/400)*100

print(end= "Percentage Mark:")
print(perc)