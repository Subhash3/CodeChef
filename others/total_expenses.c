#include<stdio.h>
int main()
{
  int t,quant,price;
  scanf("%d",&t);
  int count=0;
  while(count<t)
  {
      scanf("%d %d",&quant,&price);
      double p,k;
      k=price*quant;
      if(quant>1000)
      {
          p=k-k*0.1;
          printf("%f\n",p);
      }
      else
      {
          p=k;
    	  printf("%f\n",p);
      }
      count++;
  }
} 
