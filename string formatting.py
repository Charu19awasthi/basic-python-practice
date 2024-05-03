n=input("enter the string in mixed form upper and lower")
user=input(f"enter your choice:  \n  all capital : cap \n all samall : s \n in form of title : t \n ")
if user == "cap".lower():
    print(n.upper())
elif user == "s".lower():
    print(n.lower())
elif user == "t".lower():
    print(n.title())