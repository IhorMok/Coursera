# ==Lesson "Example logical expressions"
# n = int(input())
# isEven = n % 2 == 0
# print(isEven)
# ==
# start1 = int(input())
# finish1 = int(input())
# start2 = int(input())
# finish2 = int(input())
# answer = start1 <= finish2 and start2 <= finish1
# # isS1in2 = start2 <= start1 <= finish2
# # isF1in2 = start2 <= finish1 <= finish2
# # isS2in1 = start1 <= start2 <= finish1
# # isF2in1 = start1 <= finish2 <= finish1
# # answer = isS1in2 or isF1in2 or isS2in1 or isF2in1
# print(answer)

#====Week9 "Условный оператор"
# x = int(input())
# if x < 0:
#     x = -x
# print(x)
#= second variant
# x = int(input())
# if x >= 0:
#     print(x)
# else:
#     print(-x)

#==Week9 "and, else, if"
# x = int(input())
# y = int(input())
# if x > 0:
#     if y > 0:
#         print(1)
#     else:
#         print(-4)
# else:
#     if y > 0:
#         print(2)
#     else:
#         print(3)

# ===
x = int(input())
if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
else:
    print("Other")
