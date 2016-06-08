a=int(input("Enter the size of the list"))
b=[]
count=0
for i in range(0,a):
	b.append(int(input()))
c=int(input("Enter the no to find"))
for i in range(0,a):
    if b[i]==c:
        flag=1
        print("Searched element is present")
        break
if(flag==0):
    print("Searched element is not present ")