#include <stdio.h>
#include <stdlib.h>

#define True  1
#define False 0

int main()
{
    long long int T;

    while(T--)
    {
        long long int N, M, Q;
        scanf("%lld %lld %lld", &N, &M, &Q);
        long long int row_matrix[M], col_matrix[N];
        int flag = False, i, query;

        if(Q == 1)
        {
            flag = True;
        }
        else
        {
            if(N > M)
            {
                for(i = 0; i < N; i++)
                {
                    if(i < M)
                    {
                        row_matrix[i] = False;
                    }
                    col_matrix[i] = False;
                }
            }
            else
            {
                for(i = 0; i < M; i++)
                {
                    if(i < N)
                    {
                        row_matrix[i] = False;
                    }
                    col_matrix[i] = False;
                }
            }
        }

        for(query = 0; query < Q; query++)
        {
            // printf("Query: %d\n", query+1);
            long long int x, y;
            scanf("%lld %lld", &x, &y);

            if(flag)
            {
                break;
            }

            col_matrix[x-1] = ! (col_matrix[x-1]);
            row_matrix[y-1] = ! (row_matrix[y-1]);
        }

        if(flag)
        {
            printf("%lld\n", M+N -2);
        }
        else
        {
            long long int count = 0;
            int i, j, a;

            for(i = 0; i < N; i++)
            {
                a = col_matrix[i];
                for(j = 0; j < M; j++)
                {
                    if(a^row_matrix[j])
                    {
                        count++;
                    }
                }
            }
            printf("%lld\n", count);
        }
    }

    exit (0);
}