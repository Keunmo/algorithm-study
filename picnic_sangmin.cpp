#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int c, n, m;
int result;
bool isFriend[10][10];
bool isMatch[10];
void match(int num, int matchNum){ // ��Ʈ��ŷ Ȱ��(n�� ����� �۰� �ð��� �����)
    if(matchNum == n/2) // ¦�� ��� ��������
        result++; // �� �߰�
    else{
        if(isMatch[num]) match(num+1, matchNum); // �̹� ¦�� �ִ� ��� �������� �ѱ�
        for(int i=num+1; i<10; i++){
            if(!isFriend[num][i]) continue; // ģ���� �ƴ� ��� ������
            if(isMatch[num] || isMatch[i]) continue; // �� �� �ϳ��� ¦�� �ִ� ��� ������
            isMatch[num] = 1;
            isMatch[i] = 1;
            match(num+1, matchNum+1); // ��ͷ� ���� ����� ¦ ���θ� üũ��
            isMatch[num] = 0; // ��Ʈ��ŷ�̹Ƿ� ¦�� �ٽ� ��������
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
            isFriend[a][b] = 1; // ģ�� ����
            isFriend[b][a] = 1; // ������ �������
        }
        match(0, 0);
        cout << result << "\n";

        for(int i=0; i<10; i++){ // �ټ��� �׽�Ʈ���̽��� ���� �ʱ�ȭ
            for(int j=0; j<10; j++)
                isFriend[i][j] = 0;
            isMatch[i] = 0;
        }
        result = 0;
    }

    return 0;
}

/*
���� ����
result�� �ʱ�ȭ ���ϰ� ���������� ��� �����ع��ȴ�...
*/