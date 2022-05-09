#include <bits/stdc++.h>
using namespace std;
char board[5][5];
int c, n;
const int dx[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
const int dy[8] = {-1, 0, 1, -1, 0, 1, -1, 1};
bool inRange(int y, int x){
    if(y >= 0 && y <= 4 && x >= 0 && x <= 4) return true;
    else return false;
}
bool hasWord(int y, int x, const string& word){
    if(!inRange(y, x)) return false;
    if(board[y][x] != word[0]) return false;
    if(word.size() == 1) return true;
    for(int direction = 0; direction < 8; ++direction){
        int nextY = y + dy[direction], nextX = x + dx[direction];
        if(hasWord(nextY, nextX, word.substr(1)))
            return true;
    }
    return false;
}
int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> c;
    for(int i=0; i<c; i++){
        for(int j=0; j<5; j++){
            for(int k=0; k<5; k++){
                cin >> board[j][k];
            }
        }
        cin >> n;
        for(int j=0; j<n; j++){
            string s;
            bool isFound = false;
            cin >> s;
            for(int k=0; k<5; k++){
                for(int l=0; l<5; l++){
                    if(hasWord(l, k, s))
                        isFound = true;
                }
            }
            if(isFound)
                cout << s << " YES\n";
            else
                cout << s << " NO\n";
            isFound = false;
        }
    }

    return 0;
}