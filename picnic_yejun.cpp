#include <iostream>

// 157p

int main(void)
{
    int caseNum;
    int student_num;
    int friend_num;
    int x, y;

    std::cin >> caseNum;


    for (int i = 0; i < caseNum; i++)
    {

        scanf("%d %d", &student_num, &friend_num);

        bool pairs[student_num][student_num];

        for (int j = 0; j < friend_num; j++)
        {
            scanf("%d %d", &x, &y);
            pairs[x][y] = true;
        }
    }

    return 0;
}