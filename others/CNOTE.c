#include <stdio.h>
#include <stdlib.h>

// All constant definitions
#define True   1
#define False  0
// #define bigInt unsigned long long int

int main()
{
    int i;
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int X, Y, K, N;
        scanf("%d %d %d %d", &X, &Y, &K, &N);
        int pages_required = X - Y;
        
        // if(pages_required <= 0)
        // {
        //     printf("LuckyChef\n");
        //     continue;
        // }

        // bigInt C[N], P[N];
        int C, P;
        int flag = False;
        
        for(i = 0; i < N; i++)
        {
            scanf("%d", &P);
            scanf("%d", &C);

            if(C <= K && P >= pages_required)
            {
                // printf("Cost: %llu, Pages: %llu\n", C[i], P[i]);
                flag = True;
                break;
            }
        }
        if(flag)
        {
            printf("LuckyChef\n");
        }
        else
        {
            printf("UnluckyChef\n");
        }
    }
}
