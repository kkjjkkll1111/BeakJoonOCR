#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    for (int i = n; i > 0; i--)
    {
        for (int sp = n-i; sp > 0 ; sp--)
        {
            printf(" ");
        }        
        for (int st = 0; st < i; st++)
        {
            printf("*");
        }
        printf("\n");
    }

}