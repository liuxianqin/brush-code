n=int(input())
price_of_day1=list(map(int,input().split()))

price_of_day2=list()

for i in range(n):
	if i==0:
		price_of_day2.append((price_of_day1[0]+price_of_day1[1])//2)
	elif i==n-1:
		price_of_day2.append((price_of_day1[n-2]+price_of_day1[n-1])//2)
	else:
		price_of_day2.append(
			(price_of_day1[i-1]+price_of_day1[i]+price_of_day1[i+1])//3)
			
print(" ".join(map(str,price_of_day2)))
