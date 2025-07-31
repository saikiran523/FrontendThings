#include<stdio.h>
int main()
{
    int nr,nc , i,j,a;
    printf("rnter the number of rows & colms");
    scanf("%d %d",&nr,&nc);
    for (i=1;i<=nr;i++)
    {
        for(a=i,j=1;j<=nc;j++)
        {
             printf("%3d",a++);
        }
       printf("\n");
    }
    
}

