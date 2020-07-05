# Разность времен
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
hour_in_sec1 = h1 * 3600
minutes_in_sec1 = m1 * 60
summs_first = hour_in_sec1 + minutes_in_sec1 + s1
hour_in_sec2 = h2 * 3600
minutes_in_sec2 = m2 * 60
summs_second = hour_in_sec2 + minutes_in_sec2 + s2
print(summs_second-summs_first)
