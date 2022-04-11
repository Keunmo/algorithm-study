#include <iostream>

// 157p

int map[10][10];
int visit[10];
int n,m,ans;

void count(int state)
{
    bool finished = true;
    int start = -1;
    for (int i = 0; i < n; i++)
    {
        if (!visit[i])
        {
            finished = false;
            start = i;
            break;
        }
    }

    if (finished)
    {
        ans += 1;
        return ;
    }

    for (int j = start+1; j < n; j++)
    {
        if (!visit[start] && !visit[j] && map[start][j])
        {
            visit[start] = true;
            visit[j] = true;
            count(state+1);
            visit[start] = false;
            visit[j] = false;
        }
    }

    return ;
}

int main(void)
{
    int caseNum;
    std::cin >> caseNum;


    for (int i = 1; i <= caseNum; i++)
    {
        ans = 0;
        for (int j = 0; j < 10; j++)
        {
            visit[i] = false;
            for (int k = 0; k < 10; k++)
            {
                map[i][j] = false;
            }
        }

        std::cin >> n >> m;

        for (int j = 0; j < m; j++)
        {
            int a, b;
            std::cin >> a >> b;
            map[a][b] = true;
            map[b][a] = true;
        }

        count(0);

        std::cout << ans << std::endl;
    }

    return 0;
}