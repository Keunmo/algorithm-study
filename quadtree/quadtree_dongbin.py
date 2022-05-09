

def reverse(s):
    tmp = s[0]
    s.pop(0)
    if tmp == "b" or tmp == "w":
        return tmp

    upperLeft = reverse(s)
    upperRight = reverse(s)
    lowerLeft = reverse(s)
    lowerRight = reverse(s)
    return "x" + lowerLeft + lowerRight + upperLeft + upperRight


C = int(input())

for i in range(C):
    a = input()
    b = []
    for j in range(len(a)):
        b.append(a[j])
    print(reverse(b))


