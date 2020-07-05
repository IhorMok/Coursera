n = int(input())
first_set = set(range(1, n + 1))
nums = first_set
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == "YES":
        nums &= guess
    else:
        nums -= guess
print(' '.join([str(x) for x in sorted(nums)]))
