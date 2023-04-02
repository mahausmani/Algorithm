"""
1- Base condition
2- Smaller input
3- Choice Diagram
"""

def LCS(a,b,m,n):
    if a == "" or b == "":
        return 0
    elif a[m] == b[n]:
        return LCS(a,b,m-1,n-1) + 1
    else:
        return max(LCS(a,b,m,n-1),LCS(a,b,m-1,n))