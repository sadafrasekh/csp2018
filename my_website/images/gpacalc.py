GradeFactor = {'A':4, 'B': 3, 'C':2, 'D':1, 'F':0}
 
todo = int(raw_input("How many GPA's would you like to calculate? "))
while todo: 
    n = int(raw_input("How many courses will you input? "))
    totpoints = 0
    totunits = 0
    while n:  
        grade = raw_input("Enter grade for course, add a + to letter if it is an AP grade: " )
        units = int(raw_input("How many units was the course? "))
        totunits += units
        points = GradeFactor[grade]*units
        totpoints += points
        n -= 1
    GPA = float(totpoints) / totunits
    print("GPA is ", ("%.2f" % GPA))
    print("total points = ", totpoints)
    print("total units = ", totunits)
    todo -= 1   