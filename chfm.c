#include<stdio.h>

int main()
{
	int	T;

	scanf("%d", &T);

	long long	n, i;
	double	sum, mean, n_, sum_;

	while ( T-- > 0 )
	{
		scanf("%lld", &n);
		long long	coins[n];
		sum = 0;

		for ( i = 0; i < n; i++ )
		{
			scanf("%lld", &coins[i]);
			sum+=coins[i];
		}
		
		mean = sum/ ((double)n);

		for ( i = 0; i < n; i++ )
		{
			sum_ = sum - coins[i];
			n_ = n - 1;

			if ( mean == sum_ / n_ )
				break;
		}

		if ( i == n )
			printf("Impossible\n");
		else
			printf("%lld\n", i+1);
	}

	return 0;
}
