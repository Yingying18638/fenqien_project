# print("請輸入名字")
pers_names=input().split()
# print(pers_names)

#創建變數
n_pers=len(pers_names)
# print(n_pers)
payments=[0]*n_pers
owe=[0]*n_pers
# print(pers_names)

# 先假設都是平分題
bill=[]
while True:
    print("___付了＿＿項目＿＿元，＿＿分擔(輸入０停止)")
    A=input()
    if A!='0':
    	bill.append(A.split())
    else:
    	break
#先算帳  	
ave=0
if bill[0][3]=='all':
   for i in range(len(bill)):
       ave+=int(bill[i][2])/n_pers

for i in range(len(bill)):
	for j in range(len(pers_names)): 
		if bill[i][0]==pers_names[j]:
		    payments[j]+=int(bill[i][2])
print("帳務",payments)

for i in range(n_pers):
    owe[i]=payments[i]-ave
print("付款",owe)

# 姓名跟帳務結合成dict
Bill={}
for i in range(n_pers):
    Bill[pers_names[i]]=owe[i]
print(Bill)
P=[Bill[x] for x in Bill if Bill[x]>=0]
M=[Bill[x] for x in Bill if Bill[x]<0]

P_names=[x for x in Bill if Bill[x]>=0]
M_names=[x for x in Bill if Bill[x]<0]

#再算金流
m=len(M)
p=len(P)
flow=[[0 for _ in range(m)] for _ in range(p)]
i=0
j=0
# count=0
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
    # count+=1
    # print(count)
    if P[i]==0 and M[j]==0:
        break
print(M,P,flow)


FFF={}
for i in range(len(P_names)):
    FFF[P_names[i]]={}
    for j in range(len(M_names)):
        # for k in range(len(P_names)):
        FFF[P_names[i]][M_names[j]]=flow[i][j]
# print(FFF)

for x in FFF:
    for y in FFF[x]:
        if FFF[x][y]>0:
            print("%s給%s %d元"%(y,x,FFF[x][y]))





