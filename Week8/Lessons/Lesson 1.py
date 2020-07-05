# print(*filter(lambda x: x > 0, map(int, input().split())))
#=======
# print(*enumerate('abcde'))
#===
# print(all(map(lambda x: x > 0, map(int, input().split()))))

#=======VER1

# pas = map(int, input().split())
# sortedPas = sorted(enumerate(pas), key=lambda x: x[1])
# taxi = map(int, input().split())
# sortedTaxi = sorted(enumerate(taxi), key=lambda x: x[1], reverse=True)
# ans = zip(sortedPas, sortedTaxi)
# sortedAns = sorted(ans, key=lambda x: x[0][0])
# print(*map(lambda x: x[1][0] + 1, sortedAns))

#==================VER2
# print(
#     *map(
#         lambda x: x[1][0] + 1,
#         sorted(
#             zip(
#                 sorted(
#                     enumerate(
#                         map(
#                             int,
#                             input().split()
#                         )
#                     ),
#                     key=lambda x: x[1]),
#                 sorted(
#                     enumerate(
#                         map(
#                             int,
#                             input().split())),
#                     key=lambda x: x[1],
#                     reverse=True
#                 )
#             ),
#             key=lambda x: x[0][0]
#
#         )
#     )
# )

#================
import itertools
# print(*itertools.combinations([1, 2, 3], 2))
# print(*itertools.permutations([1, 2, 3]))
# print(*itertools.permutations([1, 2, 3], 2))
# print(*itertools.combinations_with_replacement([1, 2, 3], 2))
#=================
import functools
# prints = functools.partial(print, end=' ')
# prints(1)
# prints(2)
#===
# print(functools.reduce(lambda x, y: x + y, [1, 2, 3]))
#====
import itertools
print(*itertools.accumulate([1, 4, 3, 5], max))