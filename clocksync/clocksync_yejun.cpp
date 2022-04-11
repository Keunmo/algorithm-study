#include <iostream>
#include <algorithm>

const int INF = 9999;

int clocks[16];

static int button[10][16]={
    {1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0},
    {0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0},
    {0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1},
    {1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0},
    {1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1},
    {0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1},
    {0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1},
    {0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0},
    {0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0}
};

bool isAll(int clock[16])
{
    for (int i = 0; i < 16; i++)
    {
        if (clock[i] != 12)
        {
            return false;
        }
    }
    return true;
}

void push(int clock[16], int btn)
{
    for (int i = 0; i < 16; i++)
    {
        if (button[btn][i] == 1)
        {
            clock[i] += 3;
            if (clock[i] == 15) clock[i] = 3; 
        }
    }
}
int solve(int clock[16], int btn)
{
    if (btn == 10) return isAll(clock) ? 0 : INF;

    int res = INF;
    for (int i = 0; i < 4; i++)
    {
        res = std::min(res, i + solve(clock, btn + 1));
        push(clock, btn);
    }
    
    return res;
}

int main(void)
{
    int caseNum;
    std::cin >> caseNum;
    
    int result;

    for (int i = 0; i < caseNum; i++)
    {
        for (int j = 0; j < 16; j++)
        {
            std::cin >> clocks[j];
        }
        result = solve(clocks, 0);
        if (result >= INF) std::cout << -1;
        else std::cout << result;
        std::cout << '\n';
    }

    return 0;
}
