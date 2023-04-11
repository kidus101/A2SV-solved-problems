n = int(input())
adj_mat = []

for i in range(n):
    row = list(map(int,input().split()))
    adj_mat.append(row)

count = 0
for row in range(n):
    for col in range(len(adj_mat[0])):
        if adj_mat[row][col] == 1:
            count += 1
print(int(count/2))
