
course_1=float(input('Please enter your score:  '))

course_2=float(input('Please enter your score:  '))

course_3=float(input('Please enter your score:  '))

average= (course_1 + course_2 + course_3)/3
if average >= 17:
     print('Statuse: Greate')
elif average < 17 and average>12:
    print('Statuse: Normal')
elif average<12:
    print('Statuse: Fail')
else:
    print('Invalid character')