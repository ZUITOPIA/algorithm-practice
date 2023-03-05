// 퀵 정렬과 함께 대표적인 '분할 정복' 방법 알고리즘
// 퀵 정렬과의 공통점 : O(N * logN)의 시간복잡도를 가짐
// 퀵 정렬과의 차이점 1 : 퀵 정렬은 최악의 경우 O(N^2) | 병합 정렬은 최악의 경우에도 O(N * logN)
// 퀵 정렬과의 차이점 2 : 퀵 정렬은 pivot 값 존재 | 병합 정렬은 pivot 값 없이 항상 반으로 나눔

// 병합 정렬 : 모두 쪼개놓고 2의 배수만큼씩 합치면서 정렬함

#include <stdio.h>

int number = 8;
int sorted[8]; // 일시적인 정렬을 위해 사용되는 추가적인 배열 => 반드시 전역 변수로 선언해야 함

void merge(int a[], int m, int middle, int n){
    int i = m;
    int j = middle + 1;
    int k = m;
    // 작은 순서대로 배열에 삽입하기
    while(i <= middle && j <= n){
        if(a[i] <= a[j]){
            sorted[k] = a[i];
            i++;
        }else {
            sorted[k] = a[j]; 
            j++;
        }
        k++;
    }
    // 남은 데이터도 삽입
    if(i > middle) // 왼쪽 i 정렬이 먼저 끝났다면
    {
       for(int t = j; t <= n; t++){
            sorted[k] = a[t];
            k++;
       }
    }else{ // 오른쪽 j 정렬이 먼저 끝났다면 
        for(int t = i; t <= middle; t++){
            sorted[k] = a[t];
            k++;
        }
    }
    // 정렬된 배열을 삽입
    for(int t = m; t <= n; t++){
        a[t] = sorted[t];
    }
}

void mergeSort(int a[], int m, int n){
    if(m < n){
        int middle = (m + n) / 2;
        mergeSort(a, m, middle);
        mergeSort(a, middle + 1, n);
        merge(a, m, middle, n);
    }
}

int main(){
    int array[number] = {7,6,5,8,3,5,9,1};
    mergeSort(array, 0, number - 1);
    for(int i = 0; i < number; i++){
        printf("%d ", array[i]);
    } 
}