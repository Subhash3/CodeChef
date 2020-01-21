#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_N 1000001

int factor_frequency[MAX_N];

int main()
{
    int T, testCase;
    scanf("%d", &T);

    for(testCase = 0; testCase < T; testCase++)
    {
        int N, len = 0, max_star = -1, i;
        int num, star, fact;

        for(i = 0; i < MAX_N; i++)
        {
            factor_frequency[i] = 0;
        }

        scanf("%d", &N);

        for(i = 0; i < N; i++)
        {
            scanf("%d", &num);
            len++;

            star = 0;
            if(num == 1)
            {
                star = len-1;
            }
            else
            {
                int sq = sqrt(num);
                for(fact = 2; fact < sq+1; fact++)
                {
                    if(num%fact == 0)
                    {
                        int a, b;
                        a = fact;
                        b = num/fact;
                        factor_frequency[a-1] += 1;
                        if(a != b)
                        {
                            factor_frequency[b-1] += 1;
                        }
                    }
                }
                star = factor_frequency[num-1];
                factor_frequency[num-1] += 1;
            }
            if(max_star < star)
            {
                max_star = star;
            }
        }
        printf("%d\n", max_star);
    }

    exit (0);
}