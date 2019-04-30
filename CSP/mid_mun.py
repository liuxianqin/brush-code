n=int(input())
input_list=list(map(int,input().split()))
input_list.sort()
#print(input_list)
mid0=input_list[n //2]
mid1=input_list[n //2] 
mid2=input_list[n//2-1]
for i in input_list:
	if input_list[0]!=input_list[-1] and input_list[0]!=mid0 and input_list[0]!=mid1 and input_list[0]!=mid2 and input_list[-1]!=mid0 and input_list[-1]!=mid1 and input_list[-1]!=mid2 :
		del input_list[0]
		del input_list[-1]

if len(input_list)==0 or input_list[0]!=input_list[-1] or len(input_list)==n:
	print(-1)
elif input_list[0]==input_list[-1]:
	print(input_list[0])
#print(input_list)
