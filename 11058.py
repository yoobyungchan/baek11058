t = int(input())

d = [0] * (t+1)
for i in range(1,t+1):
    temp1 = temp2 = 0
    if i-1 >= 0:
        temp1 = d[i-1] + 1
    for j in range(1, i-2):
        if i - (j+2) >= 0:
            a = d[i-(j+2)]*(j+1)
            if temp2 < a:
                temp2 = a
    d[i] = max(temp1, temp2)

print(d[t])

