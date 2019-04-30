n=int(input())
nums=list(map(int,input().split()))
nums.sort()
#nums.reverse()
the_set=list(set(nums))
the_set.sort()
#the_set.reverse()
#print(the_set)s

re=dict(zip(the_set,map(nums.count,the_set)))
#print(re)
print(max(re,key=re.get))
