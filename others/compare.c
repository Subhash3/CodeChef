#include <stdio.h>
#include <math.h>

int main()
{
  long long int t, a, b, n;
  scanf("%lld", &t);

  while (t--)
  {
      scanf("%lld%lld%lld", &a, &b, &n);
      if (powl(a, n) > powl(b, n))
	      printf("1\n");
      else if (powl(a, n) < powl(b, n))
	      printf("2\n");
      else
	      printf("0\n");

  }
}
