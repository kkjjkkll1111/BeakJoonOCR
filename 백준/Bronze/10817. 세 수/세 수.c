#include <stdio.h>

int main(){
    int A, B, C;
    int result;
    scanf("%d %d %d", &A, &B, &C);

    if(A >= B && A >= C){ //A가 가장 클때
        if (B > C) {
            result = B;
        } else {
            result = C;
        }
        
    } else if(B >= A && B >= C) { //B가 가장클때
        if (A > C) {
            result = A;
        } else {
            result = C;
        }
    } else{
        if (A > B) {
            result = A;
        } else {
            result = B;
        }
    }
    printf("%d",result);
}