#include <stdio.h>


int main(){
    int a;
    scanf("%d", &a);
    for (int i = 1; i <= a; i++)
    {
        int j = i;
        int aa = j;
        while (j > 0)
        {
            aa += j%10;
            j = j/10;
        }
        if (aa == a)
        {
            printf("%d",i);
            break;
        } if (i == a)
        {
            printf("0");
        }
        
        
    }
    return 0;
}