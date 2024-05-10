# to find sum of tuple elements
n=input("enter the entries").split()
element=tuple(map(int,n))
c=0
for i in element:
    c+=i
print(f"your tuple is {element} \n the sum of all elements is : {c}")

# to reverse a tuple
print(f'reversed tuple is {element[::-1]}')