input_counter = 1
check = int(1)
obtained_marks = 0
credit_hours = 0
quality_points = 0
total_quality_points = 0
scgpa = 0
total_credit_hours = 0
while check != 0:
    print('Enter Subject-{} Obtained Marks'.format(input_counter))
    obtained_marks = int(input())
    print('Enter Subject-{} credit_hours'.format(input_counter))
    credit_hours = int(input())
    total_credit_hours += credit_hours
    print('Obtained Marks are : {}'.format(obtained_marks))
    input_counter +=1

    grades = 1
    if(50 <= obtained_marks <=70):
        for i in range(50,71):
          grades += 0.1
          if i == obtained_marks:
            scgpa = grades
            grades = 0
            break
    elif(obtained_marks == 71):
      scgpa = 3.05
    elif(obtained_marks == 72):
      scgpa = 3.1
    elif(obtained_marks == 73):
      scgpa = 3.15
    elif(obtained_marks == 74):
      scgpa = 3.2
    elif(obtained_marks == 75):
      scgpa = 3.3
    elif(obtained_marks == 76):
      scgpa = 3.35
    elif(obtained_marks == 77):
      scgpa = 3.4
    elif(obtained_marks == 78):
      scgpa = 3.45
    elif(obtained_marks == 79):
      scgpa = 3.5
    elif(obtained_marks == 80):
      scgpa = 3.6
    elif(obtained_marks == 81):
      scgpa = 3.65
    elif(obtained_marks == 82):
      scgpa = 3.7
    elif(obtained_marks == 83):
      scgpa = 3.8
    elif(obtained_marks == 84):
      scgpa = 3.9
    elif(obtained_marks == 80):
      scgpa = 4
    else:
      scgpa = 4

    quality_points = scgpa * credit_hours
    total_quality_points += quality_points
    print('Enter 0 to exit')
    check = int(input())

print('CGPA is {}'.format(round(total_quality_points/total_credit_hours,1)))
print('Total Quality Points are {}'.format(round(total_quality_points,1)))
print('Total Credit Hours are {}'.format(round(total_credit_hours,1)))