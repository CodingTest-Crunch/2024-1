// https://www.acmicpc.net/problem/1475

#include <iostream>
#include <algorithm>

using namespace std;

int arr[10];

int main()
{
    int room;
    cin>>room;
    
    //숫자 개수 삽입
    while(room>0) {
        arr[room%10]++;
        room/=10;
    }
    
    //숫자가 6이나 9일때 
    if(arr[6]!=arr[9]){
        if((arr[6]+arr[9])%2==0){
            int a=(arr[6]+arr[9])/2;
            arr[6]=a; arr[9]=a;
        }
        else{
            int a=(arr[6]+arr[9])/2+1;
            arr[6]=a; arr[9]=a;
        }
    }
    
    //내림차순 정렬
    sort(arr,arr+10,greater<>());
    
    //가장 큰 숫자 출력
    cout<<arr[0];
    
    return 0;
}