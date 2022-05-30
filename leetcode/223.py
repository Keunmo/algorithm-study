#https://leetcode.com/problems/rectangle-area/

def computeArea(A, B, C, D, E, F, G, H):
    xdic = {'a':[A,C], 'b':[E,G]}
    ydic = {'a':[B,D], 'b':[F,H]}
    # recAx = [A,C]
    # recAy = [B,D]
    # recBx = [E,G]
    # recBy = [F,H]
    xpoint = [A,C,E,G]
    xpoint.sort()
    ypoint = [B,D,F,H]
    ypoint.sort()
    print('xp',xpoint)
    print('yp',ypoint)
    #case0 동일
    if A==E and C==G and F==B and H==D:
        print('case0',(C-A)*(D-B))
        return (C-A)*(D-B)
    #case1 안겹침
    # elif (xpoint[:2] == [A,C]) or (xpoint[:2] == [E,G]) or (ypoint[:2] == [B,D]) or (ypoint[:2] == [F,H]):
    elif (xpoint[:2] in xdic.values()) or (ypoint[:2] in ydic.values()):
        print('case1',(C-A)*(D-B)+(G-E)*(H-F))
        return (C-A)*(D-B)+(G-E)*(H-F)
    #case2 꼭지점 하나로 겹침
    elif (A<E<C<G or E<A<G<C) and (F<B<H<D or B<F<D<H):
        print('case2',(C-A)*(D-B)+(G-E)*(H-F)-(xpoint[2]-xpoint[1])*(ypoint[2]-ypoint[1]))
        return (C-A)*(D-B)+(G-E)*(H-F)-(xpoint[2]-xpoint[1])*(ypoint[2]-ypoint[1])
    #case3 작은게 큰거 안에 쏙
    elif (A<=E<=G<=C and B<=F<=H<=D) or (E<=A<=C<=G and F<=B<=D<=H):
        print('case3',(xpoint[3]-xpoint[0])*(ypoint[3]-ypoint[0]))
        return (xpoint[3]-xpoint[0])*(ypoint[3]-ypoint[0])
    #case4 꼭지점 두개로 겹침
    else:
        print('case4', ((C-A)*(D-B)+(G-E)*(H-F))-(xpoint[2]-xpoint[1])*(ypoint[2]-ypoint[1]))
        return ((C-A)*(D-B)+(G-E)*(H-F))-(xpoint[2]-xpoint[1])*(ypoint[2]-ypoint[1])

a=-2
b=-2
c=2
d=2
e=-1
f=4
g=1
h=6

computeArea(a,b,c,d,e,f,g,h)