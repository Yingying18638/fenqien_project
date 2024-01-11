# flow備份


B=[-260,-220,75,205,200]
minus=[x for x in B if x<0]
plus=[x for x in B if x>0]
A=sorted(minus,reverse=True)
A.extend(sorted(plus))
print("負數個數",len(minus),"，","正數個數",len(plus))
print(A)
# 僅一正或一負的狀況



#
A[len(A)-1]=A[len(A)-1]+A[0]
print("X"+str(len(A)),"給","X"+'1',(-A[0]),"元")
A[0]-=A[0]
print(A)
A[len(A)-1]+=A[1]

#負數個數>1時仍要再消掉負數
    #剩偶數個正負數時，正數絕對壓得過負數
print("X"+str(len(A)),"給","X"+'2',(-A[1]),"元") 
A[1]=A[1]-A[1]   
print(A)
print("X"+str(len(A)),"給","X"+'3',(A[len(A)-1]),"元") 
print("X"+str(len(A)-1),"給","X"+'3',A[len(A)-2],"元") 

A[len(A)-1]-=A[len(A)-1]
A[len(A)-2]-=A[len(A)-2]
A[2]-=A[2]
print(A,"平衡了！")