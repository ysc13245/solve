def solution(info, n, m):
    INF=float('inf')
    l=len(info)
    
    dp=[[INF]*m for _ in range(l+1)]
    dp[0][0]=0
    
    for i in range(l):
        a,b=info[i]
        
        for j in range(m):
            
            if dp[i][j]==INF:
                continue
            
            
            na = dp[i][j] + a
            if na<n:
                dp[i+1][j]=min(dp[i+1][j],na)
            
            nb=j+b
            if nb<m:
                dp[i+1][nb] = min(dp[i+1][nb],dp[i][j])
    
    res = min(dp[l])
    
    return res if res!=INF else -1