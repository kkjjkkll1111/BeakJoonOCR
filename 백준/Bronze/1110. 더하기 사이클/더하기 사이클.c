#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int count = 0;
    int firstn = n;

    while(1)
    {
        int n1 = n / 10;
        int n2 = n % 10;
        int result = n1 + n2;
        n = n2 * 10 + result % 10;

        count++;
        if (n == firstn)
        {
            break;
        }
    }
    printf("%d", count);
    return 0;
}