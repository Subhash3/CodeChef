#include <stdio.h>
#include <stdlib.h>

#define MODULO 1000000007
#define MAX 1000001

long long int factorials[MAX];
long long int fact_factorials[MAX];

int main()
{
    int T;
    scanf("%d", &T);
    long long int fact = 1, fact_fact = 1;
    int i;

    for(i = 1; i <= MAX; i++)
    {
        factorials[i] = (fact%MODULO * i%MODULO)%MODULO;
        fact_factorials[i] = (fact%MODULO * fact_fact%MODULO)%MODULO;
        fact = factorials[i];
        fact_fact = fact_factorials[i];
    }
    while(T--)
    {
        long long int N;
        scanf("%lld", &N);   
        printf("%lld\n", fact_factorials[N+1]);
    }

    exit (0);
}