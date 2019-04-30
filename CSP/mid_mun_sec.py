n=int(input())
input_list=list(map(int,input().split()))
input_list.sort()
lower=0
higher=0
for i in range(n-1):
	
	for j in range(n-1):
		if input_list[j]<input_list[i]:
			lower=lower+1
		elif input_list[j]<input_list[i]:
			higher=higher+1
	if lower==higher:
		print(input_list[i])
    
		
