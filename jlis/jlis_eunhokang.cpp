#include <bits/stdc++.h>
#define ll long long
using namespace std;
int INF=87654321;

int T;
int a,b;
long long A[101], B[101];
int cache[101][101];

int jlis(int x,int y){
    if(x==a && y==b) return 0;
    int & res = cache[x][y];
    if(res!=-1)return res;
    res=0;
    for(int i=x+1;i<=a;++i)if(max(A[x],B[y])<A[i])res=max(res, 1+jlis(i,y));
    for(int j=y+1;j<=b;++j)if(max(A[x],B[y])<B[j])res=max(res, 1+jlis(x,j));
    return res;
}

int main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin>>T;
    while(T--){
        memset(cache, -1, sizeof(cache));
        A[0]=B[0]=LLONG_MIN;
        cin>>a>>b;
        for(int i=1;i<=a;++i)cin>>A[i];
        for(int i=1;i<=b;++i)cin>>B[i];
        cout<<jlis(0,0)<<'\n';
    }
    return 0;
}

/*
1. LIS와 같은 문제다. 다만 다른 점은, 선택할 수 있는 원소의 범위가 하나의 배열이 아닌 두 개의 배열이 된 점만 다르다.
두 부분 증가 수열을 합치는 과정을 보면 분해를 마음대로 해도 문제가 없음을 확인할 수 있으므로, 애초에 분해된 상태로 골라 합치면 된다.
2. jlis(x,y) => a배열의 x, b배열의 y에서 만들 수 있는 최장 jlis
3. 맨 앞 0번째 자리에 숫자 0을 넣어 시작 위치를 설정할 수 있도록 한다.
4. 음의 정수에 대해서도 성립해야 하므로 값을 잘 설정해야 한다.
*/