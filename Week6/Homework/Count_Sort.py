A = [int(i) for i in input().split()]


def CountSort(A):
    first_list = [0] * 101
    for i in A:
        first_list[i] += 1
    for i in range(101):
        print((str(i) + ' ') * first_list[i], end="")


CountSort(A)
