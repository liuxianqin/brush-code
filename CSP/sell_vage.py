import re
prices=[]

length=input()
length=int(length)
new_prices=[length]
price_string=input()
#print(price_string)
prices=re.findall("\d+",price_string)


for num in range(0,length):
	prices[num]=int(prices[num])




num=1
new_prices[0]=int((prices[0]+prices[1])/2)
while num<length-1:
	new_prices.append( int((prices[num]+prices[num+1]+prices[num-1])/3) )
	num+=1
new_prices.append(int((prices[length-1]+prices[length-2])/2)	)
s=""
for price in new_prices:
	s=s+str(price)+" "
print(s)

