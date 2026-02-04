def nextGreaterElement(nums):
    st=[]
    n=len(nums)
    ans=[-1]*n
    for i in range(2*n):
        idx=i%n
        while st and nums[idx]>nums[st[-1]]:
            prev=st.pop()
            ans[prev]=nums[idx]
        if i<n:
            st.append(i)
    return ans
nums=list(map(int,input("Enter nums:").split()))
print(nextGreaterElement(nums))