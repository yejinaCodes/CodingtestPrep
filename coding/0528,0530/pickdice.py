from itertools import combinations, product
dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], 
        [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]

comb = []
for i in range(2):
    comb.append([0,1,2,3,4,5])

print(list(product(*comb)))
#print(comb)
#check = list(combinations(*comb, 2))
#print(check)