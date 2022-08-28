// 가장 작은 것을 제일 앞으로 보내는 알고리즘
// 선택 정렬의 시간 복잡도 O(N^2)

#include <stdio.h>

int main(){
    int array[10] = {1, 10, 5, 8, 7, 6, 9, 4, 3, 2};
    int i, j, min, index, temp;
    
    for(i = 0; i < 10; i ++){
        printf("%d ", array[i]);
    } // 정렬 전 1 10 5 8 7 6 9 4 3 2 출력
    printf("\n"); 

    for (i = 0; i < 10 ; i ++){
        min = 999; // min은 가장 작은 값을 가져야 하는 변수이므로 처음엔 가장 큰 값으로 설정
        for(j = i; j < 10; j++){
            if(min > array[j]){
                min = array[j];
               index = j; 
            }
        }
        temp = array[i];
        array[i] = array[index];
        array[index] = temp;
    }
    for(i = 0; i < 10; i ++){
        printf("%d ", array[i]);
    } // 정렬 후 1 2 3 4 5 6 7 8 9 10 출력

    return 0;
}