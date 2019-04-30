n=int(input())
nums=list(map(int,input().split()))
nums.sort()
#print(nums)
#print(nums[n]-nums[n-1]==1)
count=0
for i in range(1,n):
	if nums[i]-nums[i-1]==1:
		count+=1
	else:
		print("NO\n")
print(count)


#不懂
