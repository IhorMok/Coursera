# Электронные часы - 2
n = int(input())
sec = n % 60 // 10
sec1 = n % 60 % 10
minutes = (n//60) % 60 // 10
minutes1 = (n//60) % 60 % 10
hour = (n//3600) % 24
print(hour, ":", minutes, minutes1, ":", sec, sec1, sep="")
