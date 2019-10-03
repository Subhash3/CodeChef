#include <stdio.h>
#include <stdlib.h>

int main()
{
  int Q, N, L, R, C, i, count, j;

  i = 0;
  scanf("%d", &N);
  char *strings[N], P;
  while(i < N)
  {
      scanf("%s", strings[i]);
      i++;
  }
  scanf("%d", &Q);
  int counts[Q];
  i = 0;
  while(i < Q)
  {
      scanf("%d%d%d%c", &L, &R, &C, &P);
      count = 0;
      for(j = L-1; j < R; j++)
      {
          if((strings[j])[C-1] == P)
	  {
	      count++;
	  }
      counts[i] = count;
      }
  }
  for (i = 0; i < Q; i++)
  {
      printf("%d\n", counts[i]);
  }

  exit(0);
}
