#include <stdio.h>
#include <stdlib.h>

int sum_div();
void swap(int *a, int *b);
int sum(int arr[]);

int ARR_SIZE;
int A, B, SA, SB, PS, SL;
int L, R;

int main()
{
    int t, res;
    scanf("%d", &t);

    while(t--)
    {
        scanf("%d %d %d %d", &A, &B, &L, &R);
        sum_div();
        PS = SA + SB;
        res = PS - SL;
        if(res < 0)
        {
            res *= -1;
        }

        if(res%2 == 0 && res%3 == 0)
        {
            printf("TRUE LOVE\n");
        }
        else if(PS%2 == 0 || PS%3 == 0)
        {
            printf("LOVE\n");
        }
        else
        {
            printf("FAKE LOVE\n");
        }
        
    }
}

int sum_div()
{
    int num;
    // LCM = lcm(A, B);

    if(R < L)
    {
        swap(&R, &L);
    }

    for(num = L; num <= R; num++)
    {
        if(num%A == 0)
        {
            SA += num;
            // printf("%d,: %d ", num, A);
        }
        if(num%B == 0)
        {
            SB += num;
            // printf("%d,: %d ", num, B);
        }
        if(num%A == 0 && num%B == 0)
        {
            SL += num;
            // printf("%d,: %d ", num, LCM);
        }
    }
    // ARR_SIZE = i;

    return 1;
    // return sum(factors);
}

void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;

    return;
}