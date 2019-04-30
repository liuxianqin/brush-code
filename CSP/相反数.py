n=int(input())
nums=list(map(int,input().split()))
count=0
for i in nums:
	if -i in nums:
		count+=1
print(count//2)
