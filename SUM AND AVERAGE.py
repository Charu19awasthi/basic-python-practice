# program for calculating sum and average of all element of list
n=input("enter the nos with space").split()
list_1=list(map(int,n))
c=0
total=len(list_1)
for i in list_1:
    c+=i
print(f"sum of all the elements is {c}")
print (f"average of list elements is {c/total}")

#program for calculating length of string
s=input("enter a string")
print(f"{s} and length of string is {len(s)}")


#program for reversing the number entered
c= (input("enter atleast 2 digit no"))
l=[]
for i in c:
    l.append(i)
l.reverse()
stri=""
for j in l:
    stri+=j
reverse_no=int(stri)
print(reverse_no)

