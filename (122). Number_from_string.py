string = input("Enter the alphanumeric string: ").split()
arr=[]
for i in string:
    if(i.isdigit()):
        arr.append(int(i))
print(max(arr))
