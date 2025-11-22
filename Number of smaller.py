n1,n2=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
k=0
ans=[]
for i,j in enumerate(arr2):
    while k<n1:
        if j<=arr1[k]:
            break
        k+=1
    ans.append(k)
print(" ".join(map(str,ans)))
