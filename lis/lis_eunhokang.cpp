#include <bits/stdc++.h>
#define ll long long
using namespace std;
int INF=87654321;

int T;
int n;
int s[501];
int cache[501];

int lis(int x){
    if(x==n) return 0;
    int & res = cache[x];
    if(res!=-1)return res;
    res=0;
    for(int i=x+1;i<=n;++i)if(s[x]<s[i])res=max(res, 1+lis(i));
    return res;
}

int main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin>>T;
    while(T--){
        memset(cache, -1, sizeof(cache));
        cin>>n;
        for(int i=1;i<=n;++i)cin>>s[i];
        cout<<lis(0)<<'\n';
    }
    return 0;
}

/*
1. 특정 위치를 포함하는 LIS를 짤 때, 이전의 선택은 이후의 선택에 영향을 주지 않는다.
2. lis(i) => i에서 만들 수 있는 최장 lis
3. 맨 앞 0번째 자리에 숫자 0을 넣어 시작 위치를 설정할 수 있도록 한다.
*/