men_str, rythm = input(), int(input())
men = [i for i in range(1, int(men_str) + 1)]
start = 0
while len(men) > 1:
    idx = (start + rythm - 1) % len(men)
    del men[idx]
    start = idx
print(*men)









