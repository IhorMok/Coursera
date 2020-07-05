a = int(input()) >= 1000
n = list(map(int, input().split()))
k = int(input())
my_list = []
for i in range(len(n)):
    my_list.append(abs(n[i]-k))
    ind_min = min(my_list)
mm = my_list.index(ind_min)
print(n[mm])
