#include<stdio.h>
int main()
{
    int N,flag=0;
    scanf("%d",&N);
    int A[N];
    for(int i=0;i<N;i++)
    scanf("%d",&A[i]);
    for(int i=0;i<N;i++)
    {
        flag=0;
        for(int j=i;j<N;j++)
        {
            if(A[i]==A[j])
            {
                flag=1;
            }
        }
        if(flag==0)
        {
            printf("%d",A[i]);
            break;
            
        }

    }
}
