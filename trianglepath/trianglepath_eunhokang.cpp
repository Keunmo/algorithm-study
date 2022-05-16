#include <bits/stdc++.h>
#define ll long long
using namespace std;
int INF=87654321;

int T;
int n;
int tri[100][100];
int cache[101][101];

int triangle(int x, int y){
    if(x==n-1)return tri[x][y];
    int & res=cache[x][y];
    if(res!=-1)return res;
    return res=tri[x][y]+max(triangle(x+1,y),triangle(x+1,y+1));
}

int main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin>>T;
    while(T--){
        memset(cache, -1, sizeof(cache));
        cin>>n;
        for(int i=0;i<n;++i)for(int j=0;j<=i;++j)cin>>tri[i][j];
        cout<<triangle(0,0)<<'\n';
    }
    return 0;
}

/*
1. 이전의 선택에 영향을 받지 않으므로 현재 위치에서 만들 수 있는 최대 합을 구하면 된다.
2. triangle(i,j) => i,j에서 만들 수 있는 최대 합
*/