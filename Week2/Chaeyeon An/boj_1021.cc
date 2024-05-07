// https://www.acmicpc.net/problem/1021

#include <iostream>
#include <deque>

using namespace std;

int main()
{
    int n,k,p,count=0;
    deque<int> st,dq;
        
    //입력
    cin>>n>>k;
    for(int i=0; i<k; i++){
        int m;
        cin>>m;
        st.push_back(m); 
    }
    
    // 덱에 삽입
    for(int i=1; i<=n; i++){ 
        dq.push_back(i);
    } 
    
    while(!st.empty()){
        if(st.front()==dq.front()) {
            st.pop_front();
            dq.pop_front();
        }
        else {
            //뽑아야 하는 원소의 위치 파악
            for(int i=0; i<dq.size(); i++){
                if(dq[i]==st.front()) p=i; 
            }
            //왼쪽이 더 가깝다면 2번실행
            if(p < (dq.size()+1)/2) {
                dq.push_back(dq.front());
                dq.pop_front();
                count++;
            }
            //오른쪽이 더 가깝다면 3번실행
            else if(p >= (dq.size()+1)/2){
                dq.push_front(dq.back());
                dq.pop_back();
                count++;
            }
        }
    }  
    
    cout<<count;
}