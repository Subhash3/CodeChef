#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int main()
{
  unsigned long int t, N;
  int P, Q;

  P = 1;

  scanf("%ld", &t);
  while(t--)
  {
      scanf("%ld", &N);
      if(N % 2 == 0)
      {
          N /= 2;
      }
      else
      {
          N = (N-1)/2;
      }
      Q = pow(10, N);
      printf("%d %d\n", P, Q);
  }
  exit (0);
}
