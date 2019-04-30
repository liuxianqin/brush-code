jump_data=list(map(int,input().split()))
score=0


for j in range(len(jump_data)-2):
	if jump_data[j+1]%2==0 and jump_data[j]%2==0:
		jump_data[j+1]=jump_data[j]+2
#print (jump_data)
for i in jump_data:
	score=score+i
print(score)

