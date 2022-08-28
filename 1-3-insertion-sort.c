// (필요할 때에만) 각 숫자를 적절한 위치에 삽입하는 알고리즘 
// 삽입 정렬의 시간 복잡도 O(N^2)
// 특징 : 정렬이 되어있다고 가정하고 시작하기 때문에 특정한 경우 속도가 매우 빠를 수도 있음

#include <stdio.h>

int main(){
    int array[10] = {1, 10, 5, 8, 7, 6, 9, 4, 3, 2};
    int i, j, temp;

    for(i = 0; i < 10; i ++){
        printf("%d ", array[i]);
    } // 정렬 전 1 10 5 8 7 6 9 4 3 2 출력
    printf("\n"); 

    for(i = 0; i < 9; i ++){
        j = i;
        while (array[j] > array[j+1])
        {
            temp = array[j];
            array[j] = array[j+1];
            array[j+1] = temp;
            j--;
        } 
    }
    for(i = 0; i < 10; i ++){
        printf("%d ", array[i]);
    } // 정렬 후 1 2 3 4 5 6 7 8 9 10 출력

    return 0;
}