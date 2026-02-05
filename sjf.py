def sjf(arr):
    arr.sort()
    n=len(arr)
    tt=0
    wt=0
    for i in range(n):
        wt+=tt
        tt+=arr[i]
    return wt//n
jobs=[1,2,3,4]
print(sjf(jobs))