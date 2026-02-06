def nextGreaterElement(nums1,nums2):
    st=[]
    nge={}
    for i in reversed(nums2):
        while st and st[-1]<=i:
            st.pop()
        if st:
            nge[i]=st[-1]
        else:
            nge[i]=-1
        st.append(i)
    ans=[]
    for i in nums1:
        ans.append(nge[i])
    return ans
nums1=list(map(int,input("Enter nums1:").split()))
nums2=list(map(int,input("Enter nums2:").split()))
print(nextGreaterElement(nums1,nums2))