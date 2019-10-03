#include <stdio.h>
     
int main()
{
  int t, c, i;
  scanf("%d", &t);
  while(t--)
  {
      scanf("%d", &c);
      for (i=2; i<=(c/2); i++)
      {
          if ( c%i == 0)
	  {
              printf("no\n" );
              break;
          }
      }
      if (i>=(c/2)) printf("yes\n" );
   }
   return 0;
} 
