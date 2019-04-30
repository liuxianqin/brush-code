n=int(input())
nums=list(map(int,input().split()))

#people=set(nums)
#print(people)

re=[]

for i in range(n):
	re.append(nums[:i].count(nums[i])+1)
#print(re)
print(" ".join(map(str,re)))
