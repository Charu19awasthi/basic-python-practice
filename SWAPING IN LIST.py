def swap(real_list):
    c=len(real_list)
    first_element=real_list[0]
    real_list[0]=real_list[c-1]
    real_list[c-1]=first_element
    return real_list
d=True 
while d:   
    n = int (input("how many values want to add in a list"))
    if n >3:
        list_1=[]
        for i in range(n):
            l=int(input("enter the value"))
            list_1.append(l)
        print(f'list created by you {list_1}')
        swap_list=swap(list_1)
        print(f"after swaping list created, {swap_list}")
    else:
        print("enter atleast 3 values")
    d=False