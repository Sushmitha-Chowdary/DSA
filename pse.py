arr=list(map(int,input().split()))
stack=[]
n=len(arr)
ans=[0]*n
for i in range(0,n):
    while(len(stack)!=0 and stack[-1]>=arr[i]):
        stack.pop()
    if(len(stack)==0):
        ans[i]=-1
    else:
        ans[i] =stack[-1]
    stack.append(arr[i])
print(ans)