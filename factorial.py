
def fac(a):
	print(a)
	if (a==1) || (a==0):
		return 1
	else:
		print(a)
		return(a*fac(a-1))
    

c=int(input('Enter the number'))
print(c)
b=fac(c)
print("computed factorial"+str(b))