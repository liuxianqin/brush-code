n=int(input())
prices=list(map(int,input().split()))
max_wave=0
wave=0
for i in range(n-1):
	wave=abs(prices[i+1]-prices[i])
	if wave>max_wave:
		max_wave=wave 
print(max_wave)
