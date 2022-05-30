#https://leetcode.com/problems/decode-string/submissions/

def decodeString(s):
    result=''
    numstk=[]
    charstk=[]
    charpop=[]
    tmp=''
    for i in s:
        print('i:',i)
        if i.isdigit(): #num
            if tmp.isdigit():  #n자리 숫자를 받아 수가 이어지는 경우
                numstk[-1]=numstk[-1]+i
            else:
                numstk.append(i)
            print('nstk:',numstk)
            print('cstk:',charstk)
        elif i == '[':
            if len(charstk)!=0 and charstk[0]!='[': #첫번째 괄호일때 == 앞에 문자만 있을때
                result = result+''.join(charstk)
                charstk=[]
                print('result0:', result)
            charstk.append(i)
            print('nstk:',numstk)
            print('cstk:',charstk)
        elif i == ']':
            while True:             # [ 만날때까지 계속 pop 
                if charstk[-1] == '[':
                    charstk.pop()
                    break
                charpop.insert(0,charstk.pop()) #charpop에 앞에서부터 스택의 pop를 넣음
            charpop = str(''.join(charpop))
            print('cpop1:',charpop)
            if '[' in charstk:  #아직 괄호를 완전히 빠져나가지 못했을때
                charstk.append(charpop * int(numstk.pop()))
                charpop=[]
                print('cpop1:',charpop)
            else:   #제일 겉의 괄호까지 다 빠져나갔을때
                result = result + charpop * int(numstk.pop())
                charpop=[]
                print('result1:',result)
            print('nstk:',numstk)
            print('cstk:',charstk)
        else: #char
            charstk.append(i)
            print('nstk:',numstk)
            print('cstk:',charstk)
        tmp=i
    result = result+''.join(charstk)    #뒤에 남은 문자들 더하기
    print('result4:',result)
    return result

s="1[1[1[A]B1[C]]]DE"
decodeString(s)
