import random
import math


def higher_power(a,b):   ## This is the function used to computer a^b in log(n) time

	if b==0:
		return 1

	if b%2==0:
		return higher_power(a,b//2)*higher_power(a,b//2)  ## if power is even return product
	else:
		return a*higher_power(a,b//2)*higher_power(a,b//2) ## else multily the given no with product




def moduar_higher_power(a,b,n):  ## It will compute moduler power
	 res=1
	 a=a%n     

	 while (b>0):   ## Compute the modular product while reducing power to half

	 	if (b&1):   ## Check if power is odd
	 		res= (res*a)%n

	 	b=b>>1   ## Binary division by 2
	 	a=(a*a)%n  
	 return res


def two_factorize(n,d):


	### Step 1:

	a=random.randrange(2,n-1)

	y= moduar_higher_power(a,d,n)

	if y==1 or y==n-1:
		return True

	while (d !=n-1):
		y=(y*y)%n 
		d*=2
		if (y==1):
			return False
		if (y==n-1):
			return True

	return False


def Miller_rabin(n,k):

	if n<=1:           ## The algo is for positive integers and one is neither prime nor composite
		return False
	if n<=3:          ## 2 and 3 are prime
		return True
	# if n%2==0:
	# 	return True

	## Performing binary search for step-0

	b= math.ceil(math.log(n))  ## Max value b can take is log(n)

	for i in range(b+1):
		a=math.ceil(math.sqrt(n))  ## Applying binary search for all integers in range 2-N^0.5
		high=a 
		low=2

		while(low<=high):
			mid=(low+high)//2
			k= higher_power(mid,i)
			if k==n:
				return False 

			if k<n:
				low=mid+1
			else:
				high=mid-1

	k=20   ## The number of iterations to be performed

	d=n-1
	while(d%2==0):
		d//=2

	for _ in range(k):
		if not two_factorize(n,d):
			return False   ### If even in one case the test returns false the no is composite
	return True            ### Returns prime with prob (1/2)^20



def main():


	print("please enter the no")
	no=int(input())
	print("Please enter the iterations")
	k=int(input())

	if(Miller_rabin(no,k)):
		print("Prime")
	else:
		print("Composite")


main()