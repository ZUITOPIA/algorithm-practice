// 2751 다른 방법으로 풀기
// quick sort 는 최악의 경우 O(N^2) 까지 나올 수 있기 때문에 C++의 algorithm을 이용하자

#include <stdio.h>
#include <algorithm>

int number, data[1000000];

int main(){
    scanf("%d", &number);
    for(int i = 0; i < number ; i++){
        scanf("%d", &data[i]);
    }
    std::sort(data, data+number);
    for(int i = 0; i < number ; i++){
        printf("%d ", data[i]);
    }
    return 0;
}