classes=int(input("enter the number of classes held"))
attend=int(input("enter the no of classes attended"))
percent=(attend/classes)*100
print(f"your attendance percent is {percent}")
if percent>=75:
    print("you are allowed to sit in class")
else:
    print("not allowed to sit in exam")