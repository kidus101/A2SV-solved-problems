n = int(input())
adj_mat = []

for i in range(n):
    row = list(map(int,input().split()))
    adj_mat.append(row)
# print(adj_mat)

adj_list = []

for row in range(n):
    arr = []
    for col in range(len(adj_mat[0])):
        if adj_mat[row][col] == 1:
            arr.append(col+1)
    adj_list.append(arr)

for i in range(n):
    print(len(adj_list[i]) , *adj_list[i])
