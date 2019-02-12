import itertools
n=5
k=3
comb = list(itertools.combinations(range(1, n+1), k))
print(comb)
answer = []
answer_temp = []
for i in range(len(comb)):
    answer.append(list(comb[i]))
print(answer)