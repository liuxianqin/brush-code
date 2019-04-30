n=int(input())
num=list(map(int,input().split()))

count=0
last=num[0]
for item in num:
	if item!=last:
		last=item
	else:
		n=n-1
		
print(n+1)

"""#数列分段
n = int(input())
a = list(map(int,input().split()))
count=1
last = a[0]
for item in a:
    if(item != last):
        count+=1
    last = item
print(count)
--------------------- 
作者：SL_logR 
来源：CSDN 
原文：https://blog.csdn.net/sl_logr/article/details/81515052 
版权声明：本文为博主原创文章，转载请附上博文链接！"""
