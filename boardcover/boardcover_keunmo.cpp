#include <iostream>
#include <string>
#include <vector>

// using std::cin;
// using std::cout;
// using std::endl;
using namespace std;

const int coverType[4][3][2] = {
    {{0,0},{1,0},{0,1}},
    {{0,0},{0,1},{1,1}},
    {{0,0},{1,0},{1,1}},
    {{0,0},{1,0},{1,-1}}
};

bool set(vector<vector<int> >& board, int y, int x, int type, int delta){
    bool ok = true;
    for (int i = 0; i < 3; i++){
        const int ny = y + coverType[type][i][0];
        const int nx = x + coverType[type][i][1];
        if ((ny < 0) || (ny >= board.size()) || (nx < 0) || (nx >= board[0].size()))
            ok = false;
        else if ((board[ny][nx] += delta) > 1)
            ok = false;
    }
    return ok;
}

int cover(vector<vector<int> >& board){
    int y = -1;
    int x = -1;
    for (int i=0; i < board.size(); i++){
        for (int j=0; j < board[i].size(); j++){
            if (board[i][j] == 0){
                y = i;
                x = j;
                break;
            }
        }
        if (y != -1)
            break;
    }
    if (y == -1)
        return 1;
    // cout << "ok" << endl;
    int count = 0;
    for (int t = 0; t < 4; t++){
        if (set(board, y, x, t, 1)){
            count += cover(board);
        }
        set(board, y, x, t, -1);
    }
    return count;
}

int main(void){
    int c, h, w = 0;
    cin >> c;
    vector<vector<vector<int>>> boards;
    for (int i = 0; i < c; i++){
        cin >> h >> w;
        vector<vector<int>> board(h, vector<int>(w, 0));
        for (int j = 0; j < h; j++){ // height
            string line;
            cin >> line;
            for (int k = 0; k < w; k++){ // width
                if (line[k]=='#')
                    board[j][k] = 1; // board[h][w]
                else 
                    board[j][k] = 0;
            }
        }
        boards.emplace_back(board);
    }
    // for (const auto& board : boards){
    //     for (const auto& line : board){
    //         for (const auto& item : line){
    //             cout << item << ' ';
    //         }
    //         cout << endl;
    //     }
    //     cout << "====" << endl;
    // }
    for (int i = 0; i < c; i++){
        // auto board = boards[i];
        // cout << board.size() << endl;
        cout << cover(boards[i]) << endl;
    }
    return 0;
}