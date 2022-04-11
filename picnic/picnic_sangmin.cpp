#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int c, n, m;
int result;
bool isFriend[10][10];
bool isMatch[10];
void match(int num, int matchNum){ // 백트래킹 활용(n이 충분히 작고 시간이 충분함)
    if(matchNum == n/2) // 짝이 모두 맞춰지면
        result++; // 값 추가
    else{
        if(isMatch[num]) match(num+1, matchNum); // 이미 짝이 있는 경우 다음으로 넘김
        for(int i=num+1; i<10; i++){
            if(!isFriend[num][i]) continue; // 친구가 아닌 경우 무시함
            if(isMatch[num] || isMatch[i]) continue; // 둘 중 하나라도 짝이 있는 경우 무시함
            isMatch[num] = 1;
            isMatch[i] = 1;
            match(num+1, matchNum+1); // 재귀로 다음 사람의 짝 여부를 체크함
            isMatch[num] = 0; // 백트래킹이므로 짝을 다시 해제해줌
            isMatch[i] = 0;
        }
    }
}
int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> c;
    for(int i=0; i<c; i++){
        cin >> n >> m;
        for(int j=0; j<m; j++){
            int a, b;
            cin >> a >> b;
            isFriend[a][b] = 1; // 친구 지정
            isFriend[b][a] = 1; // 간선은 양방향임
        }
        match(0, 0);
        cout << result << "\n";

        for(int i=0; i<10; i++){ // 다수의 테스트케이스를 위한 초기화
            for(int j=0; j<10; j++)
                isFriend[i][j] = 0;
            isMatch[i] = 0;
        }
        result = 0;
    }

    return 0;
}

/*
오답 이유
result를 초기화 안하고 무지성으로 답안 제출해버렸다...
*/