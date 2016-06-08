a=12345;
r=0;
b=len(str(a))
for i in range(0,b):
	r=r*10
	r=r+a%10
	a=a/10
print("Reversed integer is :"+str(r))