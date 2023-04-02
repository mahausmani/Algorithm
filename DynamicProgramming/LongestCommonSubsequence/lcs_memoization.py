"""
1- Base condition
2- Smaller input
3- Choice Diagram
"""
for i in range(m+2):
    for j in range(n + 1):
        if i ==0 or j == 0:
            t[i][j] = 0
        else:
            t[i][j] = -1
def LCS(a,b,m,n,t):
    if a == "" or b == "":
        return 0
    if t[m][m]!=-1:
        return t[m][n]
    elif a[n-1] == b[n-1]:
        t[m][n] = LCS(a,b,m-1,n-1,t) + 1
        return t[m][n]
    else:
        t[m][n] = max(LCS(a,b,m,n-1,t),LCS(a,b,m-1,n,t))
        return t[m][n]