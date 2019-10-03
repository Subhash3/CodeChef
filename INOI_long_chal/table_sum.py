#!/usr/bin/python3

def get_table_sums(row, N) :
    table_sums = list()
    second_row = list(range(1, N+1))
    max_score = 0
    for j in range(N) :
        for i in range(N) :
            a = row[i]
            b = second_row[i]
            if a + b > max_score :
                max_score = a + b
        table_sums.append(max_score)
        second_row.append(second_row.pop(0))
    return table_sums

N = int(input())
row = list(map(int, input().split()))
table_sums = get_table_sums(row, N)
# print(table_sums)
for i in table_sums :
    print(i, end=" ")
print()