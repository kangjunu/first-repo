sum_100 = 0
sum_1_100 = 0
for i in range(1,100001):
    sum_100 += 1
    sum_1_100 +=sum_100
print(sum_1_100)    