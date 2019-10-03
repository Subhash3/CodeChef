#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

void intersection(char s1[], char s2[]);
int isNotIn(char ch, char str[]);

char common[MAX];

int main()
{
  int t, n;
  int i, j;

  printf("t: ");
  scanf("%d", &t);
  for(i = 0; i < t; i++)
  {
      char strings[MAX][1000];
      printf("n: ");
      scanf("%d", &n);
      for(j = 0; j < n; j++)
      {
          printf("String: ");
          scanf("%s", strings[j]);
	  if(j == 0)
	  {
	      strcpy(common, strings[j]);
	  }
      }
      //strcpy(common, strings[0]);
      for(j = 1; j < n; j++)
      {
          intersection(common, strings[j]);
      }
      printf("%s, %ld\n", common, strlen(common));
  }

  exit (0);
}

void intersection(char s1[MAX], char s2[MAX])
{
  int i, j, k = 0;
  char sub_common[MAX];

  for(i = 0; i < strlen(s1); i++)
  {
      for(j = 0; j < strlen(s2); j++)
      {
          if(s1[i] == s2[j] && isNotIn(s1[i], sub_common))
	  {
	      sub_common[k] = s1[i];
	      k++;
	      break;
	  }
      }
  }
  strcpy(common, sub_common);

  return;
}

int isNotIn(char ch, char str[MAX])
{
  int i = 0;

  for(i = 0; i < strlen(str); i++)
  {
      if(str[i] == ch)
      {
          return 0;
      }
  }
  return 1;
}
