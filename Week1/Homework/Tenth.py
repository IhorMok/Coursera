rub = int(input())
rub_coint = int(input())
quantity = int(input())
count = (rub * 100 + rub_coint) * quantity
print(count // 100, count % 100)
