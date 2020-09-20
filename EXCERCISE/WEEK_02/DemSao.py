def get_input():
    n = int(input())
    s = input().split()
    a, b = [int(x) for x in s[0].split('/')]
    c, d = [int(x) for x in s[1].split('/')]

    arr = []
    for i in range(n):
        arr.append([int(x) for x in input().split()])

    low = a/b
    if d == 0:
        high = -1
    else:
        high = c/d

    return arr, low, high


def is_between(p, q, low, high):
    x_diff = q[0] - p[0]
    y_diff = q[1] - p[1]
    between = False

    if x_diff > 0:
        if ((high == -1) and (y_diff / x_diff) > low) or \
            ((high != -1) and  high > (y_diff / x_diff) > low):
            between = True

    return between


def duyettrau(arr, chain, p, low, high):
    global longest
    out_of_point = True
    for q in arr:
        if (p != q) and is_between(p, q, low, high):
            out_of_point = False
            new_chain = chain + [q]
            duyettrau(arr, new_chain, q, low, high)

    if out_of_point and len(chain) > longest:
        longest = len(chain)
        #print('new longest', chain)

#a = 1
#b = 4
#c = 3
#d = 0
#p = [2,1]
#q = [1,1]

#low = a/b
#if d == 0:
#    high = -1
#else:
#    high = c/d

arr, low, high = get_input()

longest = 0
for p in arr:
    chain = [p]
    duyettrau(arr, chain, p, low, high)

print(longest)
