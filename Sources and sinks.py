n = int(input())
ajacency_matrix = []
set_row = set()

for i in range(n):
    row = list(map(int,input().split()))

    ajacency_matrix.append(row)


list_row = []

for i in range(n):
    list_row.append(len(set(ajacency_matrix[i]))-1)

sink = []
for i in range(n):
    if list_row[i] == 0:
        sink.append(i+1)

col_list = []

for col in range(len(ajacency_matrix[0])):
    
    temp_list = []
    for row in range(len(ajacency_matrix)):
        temp_list.append(ajacency_matrix[row][col])
    col_list.append(temp_list)

list_col =[]
for i in range(n):
    list_col.append(len(set(col_list[i]))-1)

source = []
for i in range(n):
    if list_col[i] == 0:
        source.append(i+1)

print( len(source) , *source)

print(len(sink) , *sink)
