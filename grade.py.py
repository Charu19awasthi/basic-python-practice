student_marks={}
c=True
while c == True:
     key=input("enter name of student")
     marks=int(input("enter marks to add"))
     student_marks[key]=marks
     c=input("do you want to add more record if yes -(y/n?)")
     if c.lower()=='y':
          c=True
     else:
          c=False
     
print(student_marks)
item={}
for i in student_marks:
    if student_marks[i]>=91 and student_marks[i]<=100:
         item[i]='A+'
    elif student_marks[i] >=81 and student_marks[i]<=90:
         item[i]='A'
    elif student_marks[i]>=71 and student_marks[i]<=80:
         item[i]='B+'
    elif student_marks[i] >=61 and student_marks[i]<=70:
         item[i]='B'
    elif student_marks[i]>=51 and student_marks[i]<=60:
         item[i]='C'
    elif student_marks[i] >=41 and student_marks[i]<=50:
         item[i]='D'
    else:
         item[i]='F'
print(f"grades according to marks are ; {item}")    

