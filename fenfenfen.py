M=[-10,-20,-30]
P=[50,10]
m=len(M)
p=len(P)
flow=[[0 for _ in range(m)] for _ in range(p)]
i=0
j=0
count=0
#歸零
while i<m or j<p:
	if P[i]+M[j]>=0:
		P[i]+=M[j]
		#更新flow
		flow[i][j]+=abs(M[j])
		M[j]=0
		if j<p:
			j+=1
	else :
		M[j]+=P[i]
		flow[i][j]+=P[i]
		P[i]=0
		if i<m:
			i+=1
	count+=1
	print(count)
	if P[i]==0 and M[j]==0:
		break
print(M,P,flow)
for x in flow:
	for y in x:
		if y>0:
			print("給%d元"%y)
