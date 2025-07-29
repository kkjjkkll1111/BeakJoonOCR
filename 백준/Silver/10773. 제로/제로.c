#include <stdio.h>

int main(){
    int size;
    scanf("%d", &size);
    int num[size];
    int num_stack[size];

    for (int i = 0; i < size; i++)
    {
        scanf("%d", &num[i]);
        if (i == 0 && num[i] == 0)
        {
            printf("첫수는 0이 올 수 없습니다");
            i = -1;
            continue;
        }
        
        num_stack[i] = 0;
    }
    int top = 0;
    int sum = 0;
    num_stack[0] = num[0];
    for(int i = 1; i < size; i++)
    {
        if(num[i] != 0) {
            top++;
            num_stack[top] = num[i];
        } else {
            num_stack[top] = 0;
            top--;
        }

    }
    for (int j = 0; j <= top; j++)
    {
        sum += num_stack[j];
    }
    printf("%d",sum); 
}