weights = [1,2,3,4,5,6,7,8,9,10]
values =  [2,4,5,5,5,5,10,5,5,7]
n = 10
W = 29

def ks(weights, values, n, W):
    if n == 0 or W == 0:
        return 0
    if weights[n - 1] > W:
        return ks(weights, values, n-1, W)
    else:
        return max(values[n-1] + ks(weights, values, n-1, W-weights[n-1]), ks(weights, values, n-1, W))

print(ks(weights, values, n, W))



'''
How to identify this is a Dynamic Programming problem?
1- optimization: maximum weight
2- We have an option at each step; to include or not to include an item

Procedure:
1- write base condition: check for smallest valid input and value of output at that input
2- now for choice diagram, we have two options: to include an item or not to include the item.
   if we include the item, we will add its value to the total profit, search in rest of the array
   we take the maximum to see whether adding the item would give us maximum profit or not adding it would 
'''

############################ Knapsack with Memoization ##################################
n = 4
W = 20
weights = [10,2,1,3]
values = [10,5,10,10]
t = []
for i in range(n+2):
    t1 = []
    for j in range(W+2):
        if j == 0 or i ==0:
            t1.append(0)
        else:
            t1.append(-1)
    t.append(t1)
# print(t)
def ksm(weights, values, n,W,t):
    if W==0 or n==0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    elif weights[n-1]<=W:
        t[n][W] = max(values[n-1] + ksm(weights,values,n-1,W-weights[n-1],t),ksm(weights,values,n-1,W,t))
        return t[n][W]
    else:
        t[n][W] = ksm(weights,values,n-1,W,t)
        return t[n][W]

print(ksm(weights,values,n,W,t))

################### TOP DOWN #######
t = []
for i in range(n+2):
    t1 = []
    for j in range(W+2):
        if j == 0 or i ==0:
            t1.append(0)
        else:
            t1.append(-1)
    t.append(t1)
def ksmtd(weights,values,n,W,t):
    for i in range(1,n+2):
        for j in range(1,W+2):
            if weights[i-1]<W:
                t[i][j] = max(values[i-1] + t[i-1][j-1],t[])
                
