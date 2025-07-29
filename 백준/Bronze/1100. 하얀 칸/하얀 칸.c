#include <stdio.h>

int main(){
    int F = 0;
    for (int i = 0; i <= 7; i++) {
        char collum[9];
        scanf("%s", collum);
        if (i % 2 == 1) {
            for (int j = 1; j <= 7; j+=2) {
                if (collum[j] == 'F') {
                    F++;
                }
                
            }
        } else{
            for (int j = 0; j <= 6; j += 2) {
                if (collum[j] == 'F') {
                    F++;
                }
            }
        }

    }
    printf("%d",F); 
}