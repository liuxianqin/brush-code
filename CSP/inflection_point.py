n=int(input())
sales=list(map(int,input().split()))
point_num=0
for i in range(1,n-1):
	if ((sales[i]>sales[i-1] and sales[i]>sales[i+1]) or (sales[i]<sales[i-1] and sales[i]<sales[i+1])):
		point_num=point_num+1
print(point_num)
		
