#include <iostream>
// #include <string>

char board[5][5];
int dx[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
int dy[8] = {-1, 0, 1, -1, 0, 1, -1, 1};

bool hasWord(int x, int y, std::string word);

int main(void)
{
    int cases;
    int num;
    bool isWord;

    std::cin >> cases;

    for (int k = 0; k < cases; k++)
    {
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                std::cin >> board[j][i];
            }
        }

        std::cin >> num;
        std::string words[num];
        for (int i = 0; i < num; i++)
        {
            std::cin >> words[i];
        }

        for (int l = 0; l < num; l++)
        {
            std::cout << words[l];
            isWord = false;

            for (int i = 0; i < 5; i++)
            {
                for (int j = 0; j < 5; j++)
                {
                    if (hasWord(i, j, words[l]))
                    {
                        isWord = true;
                        break;
                    }
                }
                if (isWord) break;
            }
            
            if (isWord) std::cout << " YES" << std::endl;
            else std::cout <<" NO" << std::endl;
        }
    }
    return 0;
}

bool hasWord(int y, int x, std::string word)
{
    if (x > 4 || x < 0 || y > 4 || y < 0) 
    {   
        return false;
    }

    if (board[y][x] != word[0]) 
    {   
        return false;
    }

    if (word.size() == 1) 
    {
        return true;
    }

    for (int d = 0; d < 8; d++)
    {
        int nx = x + dx[d];
        int ny = y + dy[d];

        if (hasWord(ny, nx, word.substr(1)))
        {
            return true;
        }
    }
    return false;
}