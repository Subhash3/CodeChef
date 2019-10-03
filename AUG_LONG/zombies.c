#include <stdio.h>
#include <stdlib.h>

// Function prototypes
void final_radiation(long long int* initial, long long int* C, long long int N);
int is_arr_perm(long long int* radiations, long long int* zombies, long long int N);
int comp_function (const void * a, const void * b);
void printArr(long long int* arr, long long int N);

int main()
{
    long long int T, N;
    scanf("%lld", &T);
    int i, flag;

    while(T--)
    {
        scanf("%lld", &N);
        long long int initial[N], zombies[N], C[N];
        for(i = 0; i < N; i++)
        {
            initial[i] = 0;
            scanf("%lld", &C[i]);
        }

        for(i = 0; i < N; i++)
        {
            scanf("%lld", &zombies[i]);
        }

        final_radiation(initial, C, N);

        flag = is_arr_perm(initial, zombies, N);
        if(flag)
            printf("YES\n");
        else
            printf("NO\n");
    }

    exit(0);
}

void final_radiation(long long int* initial, long long int* C, long long int N)
{
    int i;
    long long int start, end;

    for(i = 0; i < N; i++)
    {
        start = i+1 -C[i] -1;
        if(start < 0)
            start = 0;
        end = i+1 + C[i]-1;
        if(end >= N)
            end = N;

        initial[start] += 1;
        if(end != N-1)
            initial[end+1] -= 1;
    }
    for(i = 1; i < N; i++)
    {
        initial[i] += initial[i-1];
    }

    return;
}

int is_arr_perm(long long int* radiations, long long int* zombies, long long int N)
{
    int i;

    qsort(radiations, N, sizeof(long long int), comp_function);
    qsort(zombies, N, sizeof(long long int), comp_function);

    for(i = 0; i < N; i++)
    {
        if(radiations[i] != zombies[i])
        {
            return 0;
        }
    }
    return 1;
}

int comp_function (const void * a, const void * b)
{
    return ( *(int*)a-*(int*)b);
}

void printArr(long long int* arr, long long int N)
{
    int i;
    for(i = 0; i < N; i++)
    {
        printf("%lld, ", arr[i]);
    }
    printf("\n");
}