# https://leetcode.com/problems/daily-temperatures/

# #Time Limit Exceeded
# def dailyTemperatures(T):
#     T.append('End')
#     days = []
#     print("T:", T)
#     today_index = -1
#     for today in T:
#         today_index += 1
#         if today == 'End':
#             break
#         count = 0
#         print("today:", today)
#         print("today_i:", today_index)
#         for findwarm in T[today_index+1:]:
#             print("findrange", T[today_index+1:])
#             count+=1
#             print("count:", count)
#             if findwarm == 'End':
#                 days.append(0)
#                 break
#             if findwarm > today:
#                 print("got it!")
#                 days.append(count)
#                 print("days:", days)
#                 break
#     print(days)
#     return days

# Time Limit Excedeed
def dailyTemperatures(T):
    day = []
    for i in range(len(T)):
        wammer = T[i]+1
        print('----\ntoday', T[i])
        if i == len(T)-1:
            day.append(0)
            break
        if T[i] < max(T[i+1:]):                         #내 뒤에 나보다 큰놈이 존재하면
            print('wammer exist')
            while True:
                print('search range',T[i+1:])
                print('wammer',wammer)
                if wammer in T[i+1:]:                   #현위치의 뒤 공간에 워머가 있으면
                    wammer_idx = T[i+1:].index(wammer)+i+1
                    print('내뒤idx:',i+1,'워머idx:',wammer_idx)
                    print('T',T)
                    print('내뒤, 워머앞',T[i+1:wammer_idx])
                    if len(T[i+1:wammer_idx])>0 and max(T[i+1:wammer_idx]) > wammer: #혹시 워머 앞에 워머 보다 큰게 있으면
                        wammer += 1                     #워머++
                        pass
                    # elif T[i+n:][0] >= wammer:          #혹시 워머보다 큰 값이 탐색범위 젤 앞에 있으면
                    #     day.append(n)
                    #     break
                    else:
                        warmday = T[i+1:].index(wammer)+1   #워머의 위치값으로 웜데이 추가.
                        day.append(warmday)
                        print('day',day)
                        break
                else:                               #워머가 탐색공간에 없으면 워머++
                    wammer += 1  
        else:
            print('no wammer')
            day.append(0)
    print(day)
    return day


# dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
dailyTemperatures([4,2,1,6,5,4,7])
                 # 0,1,2,3,4,5,6

# ans = [1, 1, 4, 2, 1, 1, 0, 0]
# ans = [3,2,1,3,2,1,0]