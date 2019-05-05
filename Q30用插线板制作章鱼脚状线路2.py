#把递归的dfs转动态规划
m=20
dfs1=[0]*(m+1)
dfs1[1]=1
for n in range(2,m+1):
    cnt=dfs1[n]
    for i in range(1,n//2+1):
        if i==n/2:
            c=dfs1[i]
            cnt+=c*(c+1)/2
        else:
            cnt+=dfs1[i]*dfs1[n-i]
    for i in range(1,n//3+1):
        for j in range(i,(n-i)//2+1):           
            if i==j and i==n-i-j:
                c=dfs1[i]
                cnt+=c*(c+1)*(c+2)/6
            elif i==j or i==n-i-j:
                c=dfs1[i]
                cnt+=c*(c+1)/2*dfs1[n-i*2]
            elif j==n-i-j:
                c=dfs1[j]
                cnt+=c*(c+1)/2*dfs1[n-j*2]
            else:
                cnt+=dfs1[i]*dfs1[j]*dfs1[n-i-j]
    dfs1[n]=cnt
    
print(dfs1[-1])    
