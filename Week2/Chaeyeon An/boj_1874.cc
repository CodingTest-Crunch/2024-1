// https://www.acmicpc.net/problem/1874

#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
 
 int k,m,point=1;
 vector<string> vt;
 stack<int> st; 
 
 //입력
 cin>>k;
 
 while(k--){
     cin>>m;
     
     while(point<=m){
         st.push(point);
         point+=1;
         vt.push_back("+");
     }
     if(st.top()==m) {
         st.pop();
         vt.push_back("-");
     }
     else{
         cout<<"NO";
         return 0;
     }
 }
 
 //출력
 for(int i=0; i<vt.size(); i++){
     cout<<vt[i]<<"\n";
 }
}