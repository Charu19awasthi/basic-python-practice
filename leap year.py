c = 'y'
while c == 'y':
    year=int(input("enter your year "))
    if year %4==0:
        if year%100==0:
            if year%400==0:
                print(f'{year} is leap year')
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is leap year")
    else:
        print(f"{year} iS not a leap year")
    c=input("do you want to check more years if yes 'y' or press any letter to exist").lower()
