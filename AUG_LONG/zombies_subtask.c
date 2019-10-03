#include <stdio.h>
#include <stdlib.h>

// Function prototypes
long long int* final_radiation(long long int* initial, long long int* C, long long int N);
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
        long long int zombies[N], initial[N], C[N];
        for(i = 0; i < N; i++)
        {
            initial[i] = N;
            scanf("%lld", &C[i]);
        }
        for(i = 0; i < N; i++)
        {
            scanf("%lld", &zombies[i]);
        }
        // printArr(C, N);
        // printArr(zombies, N);
        // printArr(initial, N);


        // printf("Caliing final radiations\n");
        final_radiation(initial, C, N);
        // printArr(initial, N);
        flag = is_arr_perm(initial, zombies, N);
        if(flag)
            printf("YES\n");
        else
            printf("NO\n");
    }

    exit(0);
}

long long int* final_radiation(long long int* initial, long long int* C, long long int N)
{
    long long int S = 0, E = N;
    int i, j;
    long long int start, end;

    for(i = 0; i < N; i++)
    {
        start = i+1 -C[i] -1;
        if(start < 0)
            start = 0;
        end = i+1 + C[i];
        if(end >= N)
            end = N;
        // printf("%lld, %lld\n", start, end);
        // printArr(initial, N);
        // printArr(C, N);

        // for(j = 0; i < N; j++)
        //     initial[j] += 1;
        for(j = S; j < start; j++)
            initial[j] -= 1;
        for(j = end; j < E; j++)
            initial[j] -= 1;
    }

    return initial;
}

int is_arr_perm(long long int* radiations, long long int* zombies, long long int N)
{
    int i;

    qsort(radiations, N, sizeof(long long int), comp_function);
    qsort(zombies, N, sizeof(long long int), comp_function);
    // printArr(radiations, N);
    // printArr(zombies, N);

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