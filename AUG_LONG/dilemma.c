#include <stdio.h>
#include <stdlib.h>

#define MAX 100000

void flip(char str[], int i, int N);
void game(char str[], int N);

int N;

int main()
{
  int T;
  char str[MAX];

  scanf("%d", &T);
  while(T--)
  {
      scanf("%s", str);
      N = sizeof(str)/sizeof(str[0]);
  }
}
