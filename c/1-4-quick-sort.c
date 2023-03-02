// 특정한 값(Pivot)을 기준으로 큰 숫자와 작은 숫자를 나누는 알고리즘
// 퀵 정렬의 시간 복잡도 O(N^2)
// 특징 : 대표적인 '분할 정복 기법' 알고리즘으로 평균 속도 O(N * logN)
// 그러나 최악의 경우(이미 전체 정렬이 되어있는 경우) -> 속도 O(N^2)까지 나올 수 있음

// 추가적인 설명
// 일반적으로 가장 앞에 있는 값을 Pivot으로 설정하고 시작
// 왼쪽에서부터 Pivot보다 큰 값 찾고, 오른쪽에서부터 Pivot보다 작은 값 찾음
// 찾은 큰 값과 작은 값 서로 위치 교환
// 두 값이 서로 엇갈려있는 경우 Pivot의 위치와 교환 -> 처음 Pivot이었던 수는 자리 고정
// 또 다시 (고정되지 않은 값들 중에서) 가장 앞에 있는 값을 Pivot으로 설정하고 같은 방식으로 진행 !!

#include <stdio.h>

int number = 10;
int data[10] = {1, 10, 5, 8, 7, 6, 9, 4, 3, 2};

void quickSort(int *data, int start, int end){
    if(start >= end){ // 원소가 1개인 경우
        return;
    }

    int key = start; // Pivot(key)은 첫번째 원소로 설정
    int i = start + 1; // 맨 왼쪽은 Pivot, 그 다음 원소의 위치를 i로 지정하기 위해 +1
    int j = end; // 맨 오른쪽 원소 위치를 j로 지정
    int temp;

    while(i <= j){
        // 큰 수와 작은 수가 엇갈릴 때까지 반복
        while (data[i] <= data[key]) 
        {   // 설정한 Pivot보다 큰 값을 만날 때 까지
            i++;
        }
        while (data[j] >= data[key] && j > start)
        {   // 설정한 Pivot보다 작은 값을 만날 때 까지
           j--;
        }
        if(i > j){ // 현재 엇갈린 상태면 키 값과 교체
            temp = data[j];
            data[j] = data[key];
            data[key] = temp;
        }else{
            temp = data[j];
            data[j] = data[i];
            data[i] = temp;
        }
        quickSort(data,start,j-1);
        quickSort(data,j+1,end);
    }
}

int main(){
    quickSort(data,0,number-1);
    for(int i = 0; i < number; i++){
        printf("%d ",data[i]);
    }
}