validMarks = 0
total = 0
mark = int(input("Enter an exam mark or '-1' to stop: "))

while mark != -1:

    if mark >= 0 and mark <=100:
        total += mark
        validMarks += 1100
        mark = int(input("Enter an exam mark or '-1' to stop: ")) 
        
        
    else:
        print("invalid mark")
        mark = int(input("Enter an exam mark or '-1' to stop: "))

print(f"Valid Marks: {validMarks}")
print(total)




