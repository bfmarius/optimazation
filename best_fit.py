import random
import timeit

weight = [random.randrange(1,50) for i in range(100)]
"weight.sort(reverse=True)"
"weight.sort()"

c = 100;
n = len(weight)

"Next fit algorithm"
def nextFit(weight, c):
    res = 0
    rem = c
    for i in range(len(weight)):
        if rem >= weight[i]:
            rem = rem - weight[i]
        else:
            res += 1
            rem = c - weight[i]
    return res

"FirstFit algorithm"
def firstFit(weight, n, c):
    res = 0
    bin_rem = [0] * n

    for i in range(n):

        j = 0
        while (j < res):
            if (bin_rem[j] >= weight[i]):
                bin_rem[j] = bin_rem[j] - weight[i]
                break
            j += 1
        if (j == res):
            bin_rem[res] = c - weight[i]
            res = res + 1
    return res


def bestFit(weight, n, c):
    # Initialize result (Count of bins)
    res = 0;
    bin_rem = [0] * n;

    for i in range(n):
        j = 0;
        min = c + 1;
        bi = 0;

        for j in range(res):
            if (bin_rem[j] >= weight[i] and bin_rem[j] -
                    weight[i] < min):
                bi = j;
                min = bin_rem[j] - weight[i];
        if (min == c + 1):
            bin_rem[res] = c - weight[i];
            res += 1;
        else:  # Assign the item to best bin
            bin_rem[bi] -= weight[i];
    return res;


print("Number of bins with Next fit:",nextFit(weight,c))
t_next=timeit.timeit(lambda: nextFit(weight, c), number=1);
print("Elapsed time:",t_next)

print("Number of bins with First fit:",firstFit(weight,n,c))
t_first=timeit.timeit(lambda: firstFit(weight, n, c), number=1);
print("Elapsed time:",t_first)

print("Number of bins with Best fit:",bestFit(weight,n,c))
t_best=timeit.timeit(lambda: bestFit(weight, n, c), number=1);
print("Elapsed time:",t_best)