n = int(input())

count = 0
for h in range(n+1):
    if '3' in str(h):
        count += 3600
        continue
    for m in range(60):
        if '3' in str(m):
            count += 60
            continue
        for s in range(60):
            if '3' in str(s):
                count += 1

print(count)